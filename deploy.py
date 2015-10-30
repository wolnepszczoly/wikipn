import os
import convert
from mkdocs.cli import build
from mkdocs.config import load_config

DEFAULT_INDEX = 'Home'

def create_index(site_dir):
    """ Creates an HTML index page to redirect to an MkDocs generated page. """
    html_code = \
        "<!DOCTYPE HTML>\n " \
        "<html>\n" \
        "\t<head>\n" \
        "\t\t<meta charset=\"UTF-8\">\n" \
        "\t\t<meta http-equiv=\"refresh\" content=\"1;url=%s/index.html\">\n" \
        % DEFAULT_INDEX + \
        "\t\t<script type=\"text/javascript\">\n" \
        "\t\t\twindow.location.href = \"%s/index.html\"\n" % DEFAULT_INDEX +\
        "\t\t</script>\n" \
        "\t</head>\n" \
        "\t<body>\n" \
        "\t\tIf you are not redirected automatically to the " \
        "%s page, follow this <a href=\"%s/index.html\">link</a>\n"\
        % (DEFAULT_INDEX, DEFAULT_INDEX) + \
        "\t</body>\n" \
        "</html>\n"

    print("Creating the index.html file...\n")
    generated_site_dir = os.path.join(site_dir, "index.html")
    index_file = open(generated_site_dir, "w")
    index_file.write(html_code)
    index_file.close()


if __name__ == '__main__':
    settings = load_config()
    convert.convert(settings['source_dir'], settings['docs_dir'])
    build.build(settings, clean_site_dir=True)
    create_index(settings['site_dir'])
    os.system('cd %s ;  git add . ; git commit -m "Wiki update" ; git push ; cd ..' % settings['site_dir'])
