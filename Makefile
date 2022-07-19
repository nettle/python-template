NAME    = $$(sed -nr "s/PROGNAME = \"(.*)\"/\1/p" src/launcher.py)
VERSION = $$(sed -nr "s/VERSION = \"(.*)\"/\1/p" src/launcher.py)
PACKAGE = $(NAME)-$(VERSION)
PYTHON  = $$([ $$(command -v python3 || true) ] && echo python3 || echo python)

all: help

clean   :                   ## Remove all intermediate files
	rm -rf venv .pytest_cache */__pycache__ */*.pyc */*.egg-info *.pyz *.zip

venv/virtualenv.pyz:
	wget -P venv https://bootstrap.pypa.io/virtualenv.pyz

venv/bin/pip: venv/virtualenv.pyz
	@echo "Creating VirtualEnv"
	@$(PYTHON) venv/virtualenv.pyz venv

venv/bin/pytest: venv/bin/pip
	. venv/bin/activate; pip install -e . pytest

venv    : venv/bin/pytest   ## Setup Virtual Environment

pytest  : venv/bin/pytest   ## Run PyTest in Virtual Environment
	. venv/bin/activate; pytest

.PHONY: test
test    :                   ## Run standard unittest
	@echo "Runnin unittests"
	@$(PYTHON) -B -m unittest discover -v -s test

pylint  :                   ## Run PyLint
	pylint */*.py

pyz     :                   ## Create Pythin zip package (pyz)
	@echo "Creating $(PACKAGE).pyz"
	@$(PYTHON) -m zipfile -c $(PACKAGE).pyz src/*

zip     :                   ## Package the source (zip)
	@echo "Creating $(PACKAGE).zip"
	@git archive HEAD --prefix=$(PACKAGE)/ --format=zip -o $(PACKAGE).zip

help    :                   ## Show this help
	@echo "Goals ($(NAME) $(VERSION)):"
	@fgrep -h "##" $(MAKEFILE_LIST) | fgrep -v fgrep | sed -r 's/(.*):.*##(.*)/   \1 -\2/'
	@echo
	@echo "Examples:"
	@echo "   make clean"
	@echo "   make test"
	@echo "   make pytest"
	@echo
