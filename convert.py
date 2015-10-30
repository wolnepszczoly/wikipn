import os
import yaml
from mkdocs.config import load_config


def change_links(text, pages_dict):
    start = text.find('[[')
    end = text.find(']]') + 2
    while start != -1 and end != 1:
        between = text[start + 2:end - 2]
	between = u'[%s](%s)' % (between, pages_dict.get(between))
        text = u''.join((text[:start], between, text[end:]))
        start = text.find('[[')
        end = text.find(']]') + 2
    return text
        

def convert(source, dest):
    pages = []
    pages_dict = {}
    for path, dirs, files in os.walk(source):
        if '.git' in path: continue
        for filename in [f for f in files if f.endswith('.md')]:
            clean_name = filename.strip().replace('-', ' ').replace('.md', '')
            rel_path = os.path.join('/'.join(path.strip().split('/')[1:]), filename)
            pages.append((path, filename))
            pages_dict[clean_name] = rel_path

    for path, filename in pages:
        new_path = path.replace(source, dest, 1)
        if not os.path.exists(new_path):
            os.makedirs(new_path)
        with open(os.path.join(path, filename), 'r') as sf:
            with open(os.path.join(new_path, filename), 'w') as df:
                data = sf.read().decode('utf-8')
                data = change_links(data, pages_dict)
                df.write(data.encode('utf-8'))
    pages = pages_dict.items()
    pages.sort(key=lambda o: (len(o[1].split('/')), o[1]))
    pages_dict = {'____': []}
    for name, path in pages:
        cur = pages_dict
        for dirname in path.split('/')[:-1]:
            clean = dirname.replace('-', ' ') 
            if clean not in cur:
                cur[clean] = {'____': []}
            cur = cur[clean]
        cur['____'].append({name: path})

    def return_pages(data):
       ret = data['____']
       for key in data:
           if key != '____':
               ret.append({key: return_pages(data[key])})
       return ret

    return return_pages(pages_dict)


if __name__ == '__main__':
    try:
    	settings = load_config()
    except:
        settings = None
    with open('mkdocs.yml') as f:
    	config = yaml.load(f)
    if settings is None:
        settings = config
    config['pages']  = convert(settings['source_dir'], settings['docs_dir'])
    with open('mkdocs.yml', 'w') as f:
    	yaml.dump(config, f)
