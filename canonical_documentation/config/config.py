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
    """Parses the supplied config file"""

    config = {}

    # Defaults for process only valiables
    config["ADDITIONAL_IMPORTS"] = ""

    config.update(default_yaml)

    with open(os.path.join(sourcedir, "conf.yaml"), "rt") as file:
        project_config = safe_load(file)
        if project_config is not None:
            config.update(project_config)

    return config

def template_config(sourcedir, config):
    """Writes configuration values to the default conf.py template"""

    result = None

    with open(os.path.join(sourcedir, default_config), "rt") as file:
        result = file.read()
        result = string.Template(result)
        result = result.substitute(config)

    return result


def check_existing_config(sourcedir):
    """Checks if a compliant conf.py exists"""

    if os.path.isfile(os.path.join(sourcedir, "conf.py")):
        with open(os.path.join(sourcedir, "conf.py"), 'rt') as file:
            try:
                ignore, keep = re.split("END OF TEMPLATE SECTION\n############################################################", file.read(), maxsplit=1)
            except:
                raise ValueError("No 'END OF TEMPLATE SECTION' delimiter found in existing config file.")
    else:
        return ""

    return keep

def write_new_config(sourcedir):
    """Writes a new configuration file based on the supplied YAML and any existing conf.py files"""

    config = parse_main_config(sourcedir)

    if 'ADDITIONAL_CONF' in config and config["ADDITIONAL_CONF"] is not None:
        with open(os.path.join(sourcedir, config["ADDITIONAL_CONF"])) as file:
            additional_conf = file.read()
            imports, additional_conf = re.split("############################################################\n# END OF IMPORTS", additional_conf, maxsplit=1)
            config["ADDITIONAL_IMPORTS"] = imports
            additional_conf = "# ADDITIONAL CONFIG" + additional_conf
    else:
        additional_conf = "" 

    result = template_config(sourcedir, config)
    delimiter = "\n############################################################\n# END OF TEMPLATE SECTION\n############################################################\n"
    existing = check_existing_config(sourcedir)

    conffile = os.path.join(sourcedir, "conf.py")
    with open(conffile, "w+t") as file:
        file.write(result + "\n" + additional_conf + delimiter + existing)

if __name__ == "__main__":
    cwd = os.getcwd()
    write_new_config(cwd)