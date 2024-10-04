import os
import sys
import subprocess
from importlib_resources import files

noxfile = default_yaml = files('canonical_documentation.tests').joinpath('noxfile.py')

def run_nox():
    print(noxfile)
    subprocess.run(["nox", "-f", noxfile])