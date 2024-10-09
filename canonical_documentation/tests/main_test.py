import os
import sys
import subprocess
import requests
from importlib_resources import files

noxfile = default_yaml = files('canonical_documentation.tests').joinpath('noxfile.py')

def get_vale_conf():

    if os.path.exists(f"{DIR}/.sphinx/styles/Canonical"):
        print("Vale directory exists")
    else:
        os.makedirs(f"{DIR}/.sphinx/styles/Canonical")

    url = "https://api.github.com/repos/canonical/praecepta/contents/styles/Canonical"
    r = requests.get(url)
    for item in r.json():
        download = requests.get(item["download_url"])
        file = open(".sphinx/styles/Canonical/" + item["name"], "w")
        file.write(download.text)
        file.close()

    if os.path.exists(f"{DIR}/.sphinx/styles/config/vocabularies/Canonical"):
        print("Vocab directory exists")
    else:
        os.makedirs(f"{DIR}/.sphinx/styles/config/vocabularies/Canonical")
    
    url = "https://api.github.com/repos/canonical/praecepta/contents/styles/config/vocabularies/Canonical"
    r = requests.get(url)
    for item in r.json():
        download = requests.get(item["download_url"])
        file = open(".sphinx/styles/config/vocabularies/Canonical/" + item["name"], "w")
        file.write(download.text)
        file.close()
    config = requests.get("https://raw.githubusercontent.com/canonical/praecepta/main/vale.ini")
    file = open(".sphinx/vale.ini", "w")
    file.write(config.text)
    file.close()

def run_nox():
    get_vale_conf()
    subprocess.run(["nox", "-f", noxfile])