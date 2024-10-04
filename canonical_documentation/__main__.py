import argparse
import sys
from . import exe



def get_args():
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

    args = parser.parse_args()

#    if len(sys.argv)==1:
#        # display help with no args
#        parser.print_help()
#        sys.exit(1)
#    else:
#        return args

    return args


if __name__ == '__main__':
    exe.entry(sys.argv[1:])
