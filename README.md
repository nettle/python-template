Name
====

What is this?
What for?


Folder structure
----------------

| Folder/File         | Description     |
| ------------------- | --------------- |
| `bin/name`          | Wrapper         |
| `name/`             | Implementation  |
| `name/__main__.py`  | Main            |
| `name/launcher.py`  | Launcher        |
| `name/parser.py`    | Parser          |
| `name/something.py` | Something       |
| `test/`             | Unit tests      |
| `README.md`         | This file       |


Optional files
--------------

| Folder/File         | Description              |
| ------------------- | ------------------------ |
| `name/__init__.py`  | Package marker           |
| `doc/`              | Documentation            |
| `LICENSE`           | Lawyering up             |
| `CHANGELOG.md`      | Version information      |
| `Makefile`          | Command automation       |
| `setup.py`          | Package and distribution |
| `requirements.txt`  | Development dependencies |


How to run
----------

Run via wrapper:

    bin/name --help

Add name/bin to `PATH`:

    PATH=$PATH:bin name --help

Run with verbose output for debugging:

    python -B name -vv


How to test
-----------

Run unit tests:

    python -B -m unittest discover -s test -vv
