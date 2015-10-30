import os
import yaml
from mkdocs.config import load_config


def change_links(text, pages_dict):
    start = text.find('[[')
    while start != -1:
        end = text.find(']]') + 2
	if end == 1: return text
        between = text[start + 2:end - 2]
	between = u'[%s](%s)' % (between, pages_dict.get(between))
        text = u''.join((text[:start], between, text[end:]))
        index = text.find('[[')
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
    pages.sort(key=lambda o: o[1])
    return [{key: value} for key, value in pages]


if __name__ == '__main__':
    settings = load_config()
    with open('mkdocs.yml') as f:
    	config = yaml.load(f)
    config['pages']  = convert(settings['source_dir'], settings['docs_dir'])
    with open('mkdocs.yml', 'w') as f:
    	yaml.dump(config, f)
