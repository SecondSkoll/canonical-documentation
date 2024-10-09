import os
import subprocess

try:
    import sphinx_autobuild
except:
    _no_autobuild = True
else:
    _no_autobuild = False

# Doesn't use Nox - so no VENV is required

def run_preview(cwd):
    
    if _no_autobuild:
        raise ImportError("sphinx-autobuild is required. Use the full installation.")
    subprocess.run(["sphinx-autobuild", cwd, '.build/html'])

if __name__ == '__main__':
    preview_test()