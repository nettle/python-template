"""
Name tools

FIXME: add description
"""

from __future__ import print_function
import argparse
import logging

import parser
import something

NAME_EXAMPLES = """
examples:

  # "Dry run" to see commands without execution:
  name --dry-run

  # Run with verbose output:
  name -vv

  ...

FIXME: add examples
"""


class NameLauncher(object):
    """
    This class is a launcher
    FIXME: add class description
    """
    def __init__(self):
        """
        Init launcher object
        """
        self.options = None

    def parse_args(self):
        """
        Parse command line arguments or show help.
        """
        args = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter,
                                       description=__doc__,
                                       epilog=NAME_EXAMPLES)
        args.prog = "name"
        args.add_argument("-v", "--verbosity",
                          default=0,
                          action="count",
                          help="increase output verbosity (e.g., -v or -vv)")
        args.add_argument("-n", "--dry-run",
                          default=False,
                          action="store_true",
                          help="just print commands without running them")
        args.add_argument("--log-format",
                          default="[Name] %(levelname)5s: %(message)s",
                          help=argparse.SUPPRESS)

        self.options = args.parse_args()

        if self.options.verbosity >= 2:
            log_level = logging.DEBUG
        elif self.options.verbosity >= 1:
            log_level = logging.INFO
        else:
            log_level = logging.WARN
        logging.basicConfig(level=log_level, format=self.options.log_format)

        logging.debug("Options: %s", self.options)

    def run(self):
        """
        Run Name tools
        """
        self.parse_args()
        try:
            logging.debug("Run...")
            parser.Parser().run()
            something.Something().run()
        finally:
            logging.debug("Done.")
