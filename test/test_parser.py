"""
Unit tests for parser
"""

import test_base


class TestParser(test_base.TestBase):
    """Unittest class for parser"""
    module_name = "parser"

    def test_parser_run(self):
        """Test parser.run()"""
        parser = self.module.Parser()
        self.assertEqual(parser.run(), True)
