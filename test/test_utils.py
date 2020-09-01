"""
Unit tests for utils
"""

import test_base


class TestUtils(test_base.TestBase):
    """Unittest class for utils"""
    module_name = "utils"

    def test_utils_execute(self):
        """Test utils execute()"""
        self.assertEqual(self.module.execute("true"), "")
        self.assertEqual(self.module.execute("echo 1"), "1\n")

    def test_utils_available(self):
        """Test utils available()"""
        self.assertTrue(self.module.available("true"))
        self.assertFalse(self.module.available("something-wrong"))
