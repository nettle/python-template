Name
====

What is this?
What for?


Folder structure
----------------

| Folder/File         | Description     |
| ------------------- | --------------- |
| `bin/name`          | Wrapper         |
| `src/`              | Implementation  |
| `src/__main__.py`   | Main            |
| `src/launcher.py`   | Launcher        |
| `src/parser.py`     | Parser          |
| `src/something.py`  | Something       |
| `test/`             | Unit tests      |
| `README.md`         | This file       |


Optional files
--------------

| Folder/File         | Description              |
| ------------------- | ------------------------ |
| `src/__init__.py`   | Package marker           |
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

Add src/bin to `PATH`:

    PATH=$PATH:bin name --help

Run with verbose output for debugging:

    python -B name -vv


How to test
-----------

Run unit tests:

    python -B -m unittest discover -s test -vv
