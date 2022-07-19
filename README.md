Python project template
=======================

This is a very simple Python project template.

Features:

- Shell execution wrapper
- Ready-to-use unittest structure
- Command automation via Makefile (try `make`)
- Simple test automation (`make test`)
- Virtual Environment support (`make venv`)
- Pytest support in Virtual Environment (`make pytest`)
- Support for executable Python zip archives (`make pyz`)
- Source Code packaging (`make zip`)


Folder structure
----------------

| Folder/File         | Description              |
| ------------------- | ------------------------ |
| `bin/name`          | Wrapper                  |
| `src/`              | Implementation           |
| `src/__main__.py`   | Main                     |
| `src/launcher.py`   | Launcher                 |
| `src/parser.py`     | Parser (example)         |
| `src/something.py`  | Something (example)      |
| `test/`             | Unit tests               |
| `test/test_base.py` | Base class for tests     |
| `test/tempdir.py`   | Temporary dir for tests  |
| `README.md`         | This file                |


Optional files
--------------

| Folder/File         | Description              |
| ------------------- | ------------------------ |
| `bin/name.bat`      | Wrapper for Windows      |
| `doc/`              | Documentation            |
| `LICENSE`           | Lawyering up             |
| `CHANGELOG.md`      | Release information      |
| `Makefile`          | Command automation       |
| `setup.py`          | Package and distribution |
| `requirements.txt`  | Development dependencies |


How to run
----------

Run via wrapper:

    bin/name --help

Add `$(PWD)/bin` to `PATH`:

    PATH=$PATH:bin name --help

Run with verbose output for debugging:

    python -B src -vv


How to test
-----------

Run all unit tests:

    python -B -m unittest discover -s test -vv

Or just one test, with verbosity:

    python -B test/test_utils.py -vvv
