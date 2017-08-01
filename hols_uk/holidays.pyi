#
# coding: utf-8
#
# Stub file for hols-uk.holidays
#
import datetime
from typing import Set, Optional


class Holidays:
    _bank_holidays: Optional[Set[datetime.date]]

    def __init__(self) -> None:
        ...

    def is_working_day(self, date: datetime.date) -> bool:
        ...

    def get_bank_holidays(self) -> Optional[Set[datetime.date]]:
        ...

    def get_working_days(self,
                         date1: datetime.date,
                         date2: datetime.date) \
            -> Set[datetime.date]:
        ...
