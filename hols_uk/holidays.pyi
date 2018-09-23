#
# coding: utf-8
#
# Stub file for hols-uk.holidays
#
import datetime
import logging
from typing import Set, Optional, Union

Date = Union[datetime.date, datetime.datetime]


class Holidays:
    _bank_holidays: Optional[Set[datetime.date]]
    logger: logging.Logger

    def __init__(self) -> None: ...

    def is_working_day(self, date: Date) -> bool: ...

    def is_bank_holiday(self, date: Date) -> bool: ...

    def get_bank_holidays(self) -> Optional[Set[datetime.date]]: ...

    def get_working_days(self, date1: Date, date2: Date) \
            -> Set[datetime.date]:
        ...
