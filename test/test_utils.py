"""
Unit tests for utils
"""
import logging

import test_base


class TestUtils(test_base.TestBase):
    """
    Unittest class for utils
    """
    MODULE_FILE_NAME = "src/utils.py"

    def test_utils_execute(self):
        """
        Test utils execute()
        """
        logging.debug("Testing execute()")
        self.assertEqual(self.module.execute("true"), "")
        self.assertEqual(self.module.execute("echo 1"), "1\n")

    def test_utils_available(self):
        """
        Test utils available()
        """
        logging.debug("Testing available()")
        self.assertTrue(self.module.available("true"))
        self.assertFalse(self.module.available("something-wrong"))


if __name__ == "__main__":
    test_base.main()
