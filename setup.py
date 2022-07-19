"""
Package configuration
"""
import os
import re
from setuptools import find_packages, setup


def search_in_file(pattern, filepath=("src", "launcher.py")):
    """
    Returns value by regex pattern in given file
    """
    filespec = [os.path.dirname(os.path.abspath(__file__))] + list(filepath)
    filename = os.path.abspath(os.path.join(*filespec))
    with open(filename, "rt") as fileobj:
        content = fileobj.read()
        version = re.search(pattern, content).group(1)
        return version


def get_version():
    """
    Get VERSION from src/launcher.py
    """
    return search_in_file(r"VERSION = \"([0-9a-z.-]+)\"")


def get_progname():
    """
    Get PROGNAME from src/launcher.py
    """
    return search_in_file(r"PROGNAME = \"(\S*)\"")


setup(
    name=get_progname(),
    version=get_version(),
    packages=find_packages(where="src"),
    package_dir={"": "src"},
)
