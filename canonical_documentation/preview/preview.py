import os
import sys
import subprocess
from importlib_resources import files

noxfile = default_yaml = files('canonical_documentation.preview').joinpath('noxfile.py')

def run_preview(cwd):
    subprocess.run(["nox", "-f", noxfile, '--', cwd])