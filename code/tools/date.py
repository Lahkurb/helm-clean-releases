# -*- coding: utf-8 -*-

"""Documentation file date.py."""

# =============================================================================
# IMPORTS
# =============================================================================

from datetime import date, datetime
from typing import NoReturn, Text, Callable
from settings.exception import ExceptionDefault

# =============================================================================
# CLASS - DATE
# =============================================================================

class Date(ExceptionDefault):

    def __init__(self, logger: Callable) -> NoReturn:
        self._logger = logger

    def date_today(self) -> Text:
        today = str(date.today())
        self.logger.info(f"Taking the current date - {today}")
        return today
    
    def days_between(self, data_first: Text, data_second: Text) -> int:
        if not isinstance(data_first, str) and not isinstance(data_first, str):  
            self.logger.error(f"We need string values... not {type(data_first)} - {type(data_second)}")

        difference = (abs((datetime.strptime(data_second, "%Y-%m-%d") - datetime.strptime(data_first, "%Y-%m-%d")).days))

        self.logger.info(f"Taking the difference between dates {data_first} - {data_second} - difference {difference} days")

        return (difference if data_first and data_second 
                            else self.raise_exception(ValueError(f"The values {data_first} - {data_second} not exist")))

    @property
    def logger(self) -> Text:
        return self._logger
