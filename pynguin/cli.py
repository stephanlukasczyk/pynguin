# This file is part of Pynguin.
#
# Pynguin is free software: you can redistribute it and/or modify
# it under the terms of the GNU Lesser General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# Pynguin is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public License
# along with Pynguin.  If not, see <https://www.gnu.org/licenses/>.
"""Pynguin is an automated unit test generation framework for Python.

This module provides the main entry location for the program execution from the command
line.
"""
import logging
import os
import sys
from typing import List, Union


def _setup_logging(
    verbose: bool = False, quiet: bool = False, log_file: Union[str, os.PathLike] = None
) -> logging.Logger:
    logger = logging.getLogger("pynguin")
    logger.setLevel(logging.DEBUG)
    if verbose:
        level = logging.DEBUG
    elif quiet:
        level = logging.NOTSET
    else:
        level = logging.INFO
    if log_file:
        file_handler = logging.FileHandler(log_file)
        file_handler.setFormatter(
            logging.Formatter(
                "%(asctime)s [%(levelname)s](%(name)s:%(funcName)s:%(lineno)d: "
                "%(message)s"
            )
        )
        file_handler.setLevel(logging.DEBUG)
        logger.addHandler(file_handler)

    if not quiet:
        console_handler = logging.StreamHandler()
        console_handler.setLevel(level)
        console_handler.setFormatter(
            logging.Formatter("[%(levelname)s](%(name)s): %(message)s")
        )
        logger.addHandler(console_handler)
    else:
        logger.addHandler(logging.NullHandler())

    return logger


def main(argv: List[str] = None) -> int:
    """Entry point of the Pynguin automatic unit test generation framework.

    :arg: argv List of command-line arguments
    :return: An integer representing the success of the program run.  0 means
    success, all non-zero exit codes indicate errors.
    """
    if argv is None:
        argv = sys.argv
    if len(argv) <= 1:
        argv.append("--help")

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
