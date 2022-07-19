"""
Base abstract class for Unit tests
"""
import imp
import logging
import os
import sys
import unittest

# Disable *.pyc files
sys.dont_write_bytecode = True


class TestBase(unittest.TestCase):
    """
    Unittest base abstract class
    """

    # NOTE: MODULE_FILE_NAME must be defined in derived class!
    # e.g.: MODULE_FILE_NAME = "package/module.py"
    MODULE_FILE_NAME = None
    # Project root dir (default: ..)
    ROOT_DIR = os.pardir

    @classmethod
    def setUpClass(cls):
        """
        Load module, save environment
        """
        # Save environment and location
        cls.location = os.path.abspath(os.path.dirname(__file__))
        cls.save_env = os.environ
        cls.save_cwd = os.getcwd()
        # Load module under test
        cls.module_name = cls.MODULE_FILE_NAME
        cls.module_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, cls.module_name))
        cls.module_dir = os.path.dirname(cls.module_path)
        sys.path.insert(0, cls.module_dir)
        cls.module_name = os.path.splitext(os.path.basename(cls.module_name))[0]
        cls.module = imp.load_source(cls.module_name, cls.module_path)
        # Move to project root
        cls.root_path = os.path.abspath(os.path.join(os.path.dirname(__file__), cls.ROOT_DIR))
        os.chdir(cls.root_path)

    @classmethod
    def tearDownClass(cls):
        """
        Restore environment
        """
        os.chdir(cls.save_cwd)
        os.environ = cls.save_env


def setup_logging():
    """
    Setup logging level for test execution
    """
    # Enable debug logs for tests if "super verbose" flag is provided
    if "-vvv" in sys.argv:
        logging.basicConfig(
            level=logging.DEBUG,
            format="[TEST] %(levelname)5s: %(message)s")


def main():
    """
    Run unittest
    """
    setup_logging()
    unittest.main(buffer=True)
