# canonical-documentation

This is a basic POC of a Python driven [Starter Pack](https://github.com/canonical/sphinx-docs-starter-pack/) entrypoint.

# Overview

This repository creates a Python application that will function as an entrypoint to Canonical's Sphinx based documentation tooling.

Only initial POC / alpha features are currently in place.

```
usage: canonical-documentation [-h] {init,yaml,config,update,test} ...

Build and maintain Canonical documentation

positional arguments:
  {init,yaml,config,update,test}
                        sub-command help
    init                initiatlise documentation set
    yaml                generate a YAML file with required configuration values
    config              generate a conf.py file from a YAML configuration
    update              update Starter Pack based documentation
    test                run testing on a documentation set

options:
  -h, --help            show this help message and exit
```

## Init

Note: Not currently implemented.

The `init` command will deploy a new set of files for the creation of a new documentation set.

## Yaml

Note: Basic POC implemented

The `yaml` command will create a YAML configuration file with default values for use with the `config` command.

## Config

Note: Not currently implemented.

The `config` command will parse a YAML configuration file, and any existing `conf.py` file, and deploy a new `conf.py` file with updated configuration.

## Update

Note: Not currently implemented.

The `update` command will update existing Starter Pack documentation to a newer version, if one is available.

## Test

Note: Minimal POC implemented

The `test` command will run documentation validation tests on a local documentation set.

Tests are implemented with [Nox](https://nox.thea.codes/en/stable/), and are contained in this repository, removing the need for local testing and operational files.

## Preview

Note: Minimal POC implemented - needs some Starter Pack standard packages to function on SP doc sets.

The `preview` command runs `sphinx-autobuild` and provides a local preview of the documetnation set.

## PDF

Note: To be added

The `PDF ` command deploys a PDF from an appropriately configured documentation set.