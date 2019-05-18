SHELL:=bash
.PHONY: distribution develop build install \
	upload pip-install pip-uninstall clean

PROJECT:=$(shell git rev-parse --show-toplevel)
PROJECTNAME:=$(shell basename `git rev-parse --show-toplevel`)
PYTHON:=python
PIP:=pip

###############################
# # Other related targets...  #
###############################
# start here...



######################################
# # Python packaging related targets #
######################################

SOURCES:= \
	MANIFEST.in \
	requirements.txt \
	PYPI_README.md \
	$(shell find $(PROJECT) -name '*.py')

distribution: $(SOURCES)
	$(PYTHON) setup.py sdist bdist_wheel

develop:
	$(PYTHON) setup.py develop

build:
	$(PYTHON) setup.py build

install:
	$(PYTHON) setup.py install

upload: $(SDIST_TAR)
	twine upload --skip-existing dist/*

pip-install:
	$(PIP) install --user --no-cache-dir --force-reinstall $(PROJECTNAME)

pip-uninstall:
	$(PIP) uninstall $(PROJECTNAME)

# clean
clean:
	$(PYTHON) setup.py clean --all
	-rm -rf $(PROJECTNAME).egg-info
	-rm -rf dist/
	find . -name '*.pyc' -exec rm -f {} +
	find . -name '*.pyo' -exec rm -f {} +
	find . -name '*~' -exec rm -f  {} +
