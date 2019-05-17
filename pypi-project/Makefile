SHELL:=bash

PROJECT:=$(shell git rev-parse --show-toplevel)
PROJECTNAME:=$(shell basename `git rev-parse --show-toplevel`)
PYTHON:=python
PIP:=pip

SOURCES:= \
	MANIFEST.in \
	requirements.txt \
	PYPI_README.md \
	$(shell find $(PROJECT) -name '*.py')

.PHONY: distribution
distribution: $(SOURCES)
	$(PYTHON) setup.py sdist bdist_wheel

.PHONY: develop
develop:
	$(PYTHON) setup.py develop

.PHONY: build
build:
	$(PYTHON) setup.py build

.PHONY: install
install:
	$(PYTHON) setup.py install

.PHONY: upload
upload: $(SDIST_TAR)
	twine upload --skip-existing dist/*

.PHONY: clean
clean:
	$(PYTHON) setup.py clean --all
	-rm -rf $(PROJECTNAME).egg-info
	-rm -rf dist/

.PHONY: pip-install
pip-install:
	$(PIP) install --user --no-cache-dir --force-reinstall $(PROJECTNAME)

.PHONY: pip-uninstall
pip-uninstall:
	$(PIP) uninstall $(PROJECTNAME)
