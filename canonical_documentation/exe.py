import subprocess
import sys
import argparse
from yaml import safe_load, dump
from importlib_resources import files
from . import defaults

from canonical_documentation.tests.main_test import run_nox


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

    return parser

def interactive():
    raise Exception("Placeholder for interactive function")

def init():
    raise Exception("Placeholder for init function")

def yaml():
    print(default_yaml)
    with open("conf.yaml", "w+") as file:
        file.write(dump(default_yaml))

def config(file):
    raise Exception("Placeholder for config function")

def update(root):
    raise Exception("Placeholder for update function")

def test(scope):
    run_nox()

def entry(argv = (), /):

    if not argv:
        argv = sys.argv[1:]

    parser = arg_parse()
    args = parser.parse_args(argv or sys.argv[1:])

    if vars(args)['arg'] == "none":
        interactive()
        pass

    elif vars(args)['arg'] == "init":
        init()


    elif vars(args)['arg'] == "yaml":
        yaml()

    elif vars(args)['arg'] == "config":
        config()

    elif vars(args)['arg'] == "update":
        update()

    elif vars(args)['arg'] == "test":
        test('x')

    else:
        raise Exception("Entry ARG exception, please raise an issue on GitHub.")


if __name__ == "__main__":
    entry(sys.argv[1:])