"""
Base class for all unit tests
"""

import imp
import os
import unittest


class TestBase(unittest.TestCase):
    """
    Abstract unittest TestBase class
    """
    MODULE_DIR = "src"    # Change to you dir
    MODULE_NAME = "base"  # IMPORTANT! Redefine MODULE_NAME in your subclass

    @classmethod
    def setUpClass(cls):
        """
        Load module
        """
        # NOTE: MODULE_NAME must be defined in subclasses
        cls.module_path = os.path.join(cls.MODULE_DIR, cls.MODULE_NAME + ".py")
        cls.module_path = os.path.abspath(
            os.path.join(os.path.dirname(__file__), os.pardir, cls.module_path))
        cls.module = imp.load_source(cls.MODULE_NAME, cls.module_path)
