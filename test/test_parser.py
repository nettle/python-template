"""
Unit tests for parser
"""

import test_base


class TestParser(test_base.TestBase):
    """
    Unittest class for parser module
    """
    MODULE_FILE_NAME = "src/parser.py"

    def test_parser_run(self):
        """
        Test parser.run()
        """
        parser = self.module.Parser()
        self.assertEqual(parser.run(), True)


if __name__ == "__main__":
    test_base.main()
