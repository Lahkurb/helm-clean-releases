# -*- coding: utf-8 -*-

"""Documentation file os.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from operator import itemgetter
from abc import ABCMeta, abstractmethod
from os import path, makedirs, stat, listdir
from typing import NoReturn, Text

# =============================================================================
# CLASS - OS
# =============================================================================

class OS(object):

    @staticmethod
    def check_if_is_dir(directory: Text) -> bool:
        try:
            return True if path.isdir(directory) else False
        except Exception as error:
            print(f"\nError general exception in check if the directory {directory} exist in the system - {error}")

    @staticmethod
    def check_if_is_file(file: Text) -> bool:
        try:
            return True if path.isfile(file) else False
        except Exception as error:
            print(f"\nError general exception in check if the file {file} exist in the system - {error}")

    @staticmethod
    def join_directory_and_file(directory: Text, file: Text) -> Text:
        try:
            return path.join(directory, file)
        except Exception as error:
            print(f"\nError general exception in join the directory {directory} with the file {file} - {error}")

    @staticmethod
    def create_directory(directory: Text) -> NoReturn:
        try:
            makedirs(directory)
        except OSError:
            print(f"\nError in create the directory {directory} in the system - {error}")
        except Exception as error:
            print(f"\nError general exception in create the directory {directory} in the system - {error}")

    @staticmethod
    def create_file(file: Text) -> NoReturn:
        try:
            with open(file, mode="w"): pass
        except Exception as error:
            print(f"\nError general exception create the file {file} in the system - {error}")
