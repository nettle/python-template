"""
Temporary dir
"""
import logging
import shutil
import os
import sys
import tempfile

# Disable *.pyc files
sys.dont_write_bytecode = True


class TemporaryDir:
    """
    Safely creates and destroys temporary folder
    """
    def __init__(self):
        self._temp_dir = None

    def __enter__(self):
        self._temp_dir = tempfile.mkdtemp()
        logging.debug("Created %s", self._temp_dir)
        return self._temp_dir

    def __exit__(self, tipe, value, traceback):
        shutil.rmtree(self._temp_dir)
        logging.debug("Removed %s", self._temp_dir)

    def create_file(self, filename, data):
        """
        Create data file in temp dir
        """
        fullname = os.path.join(self._temp_dir, filename)
        with open(fullname, "w") as fileobj:
            fileobj.write(data)
        return fullname
