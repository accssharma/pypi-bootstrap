SHELL:=bash

default:all

PROJECT:=$(shell git rev-parse --show-toplevel)
PROJECTNAME:=$(shell basename `git rev-parse --show-toplevel`)

.PHONY: distribution
distribution: $(SOURCES)
	python setup.py sdist bdist_wheel

.PHONY: develop
develop:
	python setup.py develop

.PHONY: build
build:
	python setup.py build

.PHONY: upload
upload: $(SDIST_TAR)
	twine upload --skip-existing dist/*

.PHONY: pip-install
pip-install:
	pip install --user --no-cache-dir --force-reinstall $(PROJECTNAME)

.PHONY: clean
clean:
	python setup.py clean --all
	-rm -rf $(PROJECTNAME).egg-info
	-rm -rf dist/
	pip uninstall $(PROJECTNAME)
