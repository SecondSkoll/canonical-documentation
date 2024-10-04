VENV_DIR = .venv
VENV = $(VENV_DIR)/bin/activate

venv:
	python3 -m venv $(VENV_DIR)
	@. $(VENV); pip install -r requirements.txt
	@. $(VENV); pip install -r canonical_documentation/requirements.txt

canonical-documentation: venv
	@. $(VENV); python -m build

install: canonical-documentation
	@. $(VENV); python -m pip install dist/canonical_documentation-0.1.tar.gz

run: install
	@. $(VENV); canonical-documentation yaml

clean:
	rm -r $(VENV_DIR) || true
	rm -r dist || true
	rm -r canonical_documentation.egg-info || true
