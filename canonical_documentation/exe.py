import subprocess
import sys
import argparse
from yaml import safe_load, dump
from importlib_resources import files
from . import defaults
import os

from canonical_documentation.tests.main_test import run_nox
from canonical_documentation.preview.preview import run_preview
from canonical_documentation.config.config import write_new_config


default_yaml = safe_load(files(defaults).joinpath('default.yaml').read_text())


def arg_parse():
    parser = argparse.ArgumentParser(
        prog='canonical-documentation',
        description="Build and maintain Canonical documentation")
    parser.set_defaults(arg='none')

    subparsers = parser.add_subparsers(help='sub-command help')

    parser_init = subparsers.add_parser('init', help='initiatlise documentation set')
    parser_init.add_argument('-d', '--directory', required=False, default='', help='config file location')
    parser_init.set_defaults(arg='init')

    parser_yaml = subparsers.add_parser('yaml', help='generate a YAML file with required configuration values')
    parser_yaml.set_defaults(arg='yaml')

    parser_config = subparsers.add_parser('config', help='generate a conf.py file from a YAML configuration')
    parser_config.add_argument('-y', '--yaml', help='generate conf.py from a YAML configuration')
    parser_config.set_defaults(arg='config')

    parser_update = subparsers.add_parser('update', help='update Starter Pack based documentation')
    parser_update.add_argument('-d', '--directory', required=False, default='', help='config file location')
    parser_update.set_defaults(arg='update')

    parser_test = subparsers.add_parser('test', help='run testing on a documentation set')
    parser_test.set_defaults(arg='test')

    parser_test = subparsers.add_parser('preview', help='run a local preview')
    parser_test.set_defaults(arg='preview')

    return parser

def interactive():

    # TODO: [Priority low] - Develop interactive function

    raise Exception("Placeholder for interactive function")

def init():

    # TODO: [Priority medium] - Put demo docs together defining the files needed for init
    # TODO: [Priority medium] - Develop init function
    # TODO: [Priority low] - Options for RST/MD based docs

    raise Exception("Placeholder for init function")

def yaml():

    # TODO: [Priority medium] - Extend yaml file to all defaults

    print(default_yaml)
    with open("conf.yaml", "w+") as file:
        file.write(dump(default_yaml))

def config(cwd):

    # TODO: [Priority medium] - Move to optional conf.py addition through yaml file
    # TODO: [Priority medium] - Split optional conf.py into logical sections for ingestion and Python validation (imports at top, etc.)

    write_new_config(cwd)

def update(root):

    # TODO: [Priority low] - Develop update function

    raise Exception("Placeholder for update function")

def test(scope):

    # TODO: [Priority high] - Develop full tests

    run_nox()

def preview(cwd):

    # TODO: [Priority medium] - Move preview function to optional install

    preview_test(cwd)

def entry(argv = (), /):

    if not argv:
        argv = sys.argv[1:]

    parser = arg_parse()
    args = parser.parse_args(argv or sys.argv[1:])

    cwd = os.getcwd()
    if os.path.isdir('.sphinx'):
        sphinx_dir = '.sphinx/'

    if vars(args)['arg'] == "none":
        interactive()
        pass

    elif vars(args)['arg'] == "init":
        init()


    elif vars(args)['arg'] == "yaml":
        yaml()

    elif vars(args)['arg'] == "config":
        config(cwd)

    elif vars(args)['arg'] == "update":
        print(args)
        update(vars(args)['directory'])

    elif vars(args)['arg'] == "test":
        test('x')

    elif vars(args)['arg'] == "preview":
        preview(cwd)

    else:
        raise Exception("Entry ARG exception, please raise an issue on GitHub.")


if __name__ == "__main__":
    print("DEBUG MODE ON")
    print(sys.argv)
    entry(sys.argv[1:])