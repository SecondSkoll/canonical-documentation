import os
from yaml import safe_load
import datetime
from importlib_resources import files
import re
import string

default_yaml = safe_load(files('canonical_documentation.defaults').joinpath('default.yaml').read_text())
default_config = files('canonical_documentation.defaults').joinpath('default-config.txt')
default_latex_config = files('canonical_documentation.defaults').joinpath('default-latex-config.txt')

def parse_main_config(sourcedir):

    config = {}

    config.update(default_yaml)

    with open(os.path.join(sourcedir, "conf.yaml"), "rt") as file:
        project_config = safe_load(file)
        if project_config is not None:
            config.update(project_config)

    return config

def template_config(sourcedir):

    config = parse_main_config(sourcedir)
    result = None

    with open(os.path.join(sourcedir, default_config), "rt") as file:
        result = file.read()
        result = string.Template(result)
        result = result.substitute(config)

    return result


def check_existing_config(sourcedir):

    if os.path.isfile(os.path.join(sourcedir, "conf.py")):
        with open(os.path.join(sourcedir, "conf.py"), 'rt') as file:
            ignore, keep = re.split("END OF TEMPLATE SECTION", file.read(), maxsplit=1)
    else:
        return ""

    return keep

def write_new_config(sourcedir):

    result = template_config(sourcedir)
    delimiter = "\n# END OF TEMPLATE SECTION"
    existing = check_existing_config(sourcedir)

    conffile = os.path.join(sourcedir, "conf.py")
    with open(conffile, "w+t") as file:
        file.write(result + delimiter + existing)

if __name__ == "__main__":
    cwd = os.getcwd()
    write_new_config(cwd)