import os
from mkdocs.config import load_config


def change_links(text):
    start = text.find('[[')
    while start != -1:
        end = text.find(']]') + 2
	if end == 1: return text
        between = text[start + 2:end - 2]
	between = '[%s](%s)' % (between, between.replace(' ', '-') + '.md')
        text = ''.join((text[:start], between, text[end:]))
        index = text.find('[[')
    return text
        

def convert(source, dest):
    for path, dirs, files in os.walk(source):
        if '.git' in path: continue
        for filename in [f for f in files if f.endswith('.md')]:
            new_path = path.replace(source, dest, 1)
            if not os.path.exists(new_path):
                os.makedirs(new_path)
            with open(os.path.join(path, filename), 'r') as sf:
                with open(os.path.join(new_path, filename), 'w') as df:
                    data = sf.read()
                    data = change_links(data)
                    df.write(data)


if __name__ == '__main__':
    settings = load_config()
    convert(settings['source_dir'], settings['docs_dir'])
