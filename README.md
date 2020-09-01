Name
====

What is this?
What for?


Folder structure
----------------

| Folder/File         | Description     |
| ------------------- | --------------- |
| `bin/name`          | Wrapper         |
| `test/`             | Unit tests      |
| `name/`             | Implementation  |
| `name/__main__.py`  | Main            |
| `name/launcher.py`  | Launcher        |
| `name/parser.py`    | Parser          |
| `name/something.py` | Something       |
| `README.md`         | This file       |


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

