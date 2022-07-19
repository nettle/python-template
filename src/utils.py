"""
Common utilities
"""

import logging
import shlex
import subprocess


def execute(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE):
    """
    Run shell command
    """
    if isinstance(command, list):
        cmd = command
    else:
        cmd = shlex.split(command)
    try:
        process = subprocess.Popen(cmd, stdout=stdout, stderr=stderr)
        out, _ = process.communicate()
        return out.decode("utf-8", errors="ignore")
    except KeyboardInterrupt:
        logging.error("Interrupted!")
        return ""


def available(tool):
    """
    Return True if tool available
    """
    return bool(execute("which " + tool))
