import os
import subprocess

# Doesn't use Nox - so no VENV is required

def run_preview(cwd):
    subprocess.run(["sphinx-autobuild", cwd, '.build/html'])

if __name__ == '__main__':
    preview_test()