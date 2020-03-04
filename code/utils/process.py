# -*- coding: utf-8 -*-

"""Documentation file process.py."""

# =============================================================================
# IMPORTS
# =============================================================================

import subprocess
from typing import NoReturn, Text, Callable

# =============================================================================
# CLASS - DATE
# =============================================================================

class Process(object):

    def __init__(self, logger: Callable) -> NoReturn:
        self._logger = logger

    def run_command(self, command: Text) -> Text:
        try:
            if not isinstance(command, str):
                raise ValueError(f"We spec a string value, not {type(command)}")
            process = subprocess.Popen(command, stdin=subprocess.PIPE, stdout=subprocess.PIPE, shell=True, universal_newlines=True)
            output, errors = process.communicate()
            if process.returncode != 0: 
                self.logger.error(f"Run command failed - status returncode - {process.returncode} - {error}")
            return (output, errors)
        except subprocess.CalledProcessError as error:
            self.logger.error(f"Subprocess error when run the command {command} - {error}")
        except Exception as error:
            self.logger.error(f"Error general exception in run the command {command} - {error}")

    @property
    def logger(self) -> Text:
        return self._logger
