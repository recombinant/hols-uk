#
# coding: utf-8
#
import csv
import datetime
from operator import itemgetter
from pathlib import Path


# This module only requires the hols-uk.csv which is a text file
# (although it can be edited with Excel)
#
# There is a routine to import .ics calendar files and another to dump
# the csv in ics2csv.py
#
class Holidays:
    def __init__(self):
        self._bank_holidays = None

    def is_working_day(self, date):
        """
        Assuming that Sat & Sun are not working days and that
        all Bank holidays are not working days.

        Returns: True if day is working day.
        """
        assert isinstance(date, datetime.date)
        if date.weekday() in [5, 6]:  # Saturday, Sunday
            return False
        else:
            return date not in self.get_bank_holidays()

    def is_bank_holiday(self, date):
        return date in self.get_bank_holidays()

    def get_bank_holidays(self):
        if self._bank_holidays is None:
            if datetime.date.today() > datetime.date(2018, 1, 1):
                print('visit https://www.gov.uk/bank-holidays')
                print('for the latest bank holidays')

            holidays = set()
            csv_path = Path(__file__).parent / 'hols-uk.csv'
            if csv_path.is_file():
                with csv_path.open('rt', newline='', encoding='utf-8') as fs:
                    data = csv.DictReader(fs, dialect='excel')
                    data = map(itemgetter('Date'), data)
                    data = filter(bool, data)
                    data = (datetime.datetime.strptime(day, '%d-%b-%Y').date() for day in data)
                    holidays = {*data}
            self._bank_holidays = holidays

        return self._bank_holidays

    def get_working_days(self, date1, date2):
        """
        Number of working days in the (inclusive) interval
        between date1 and date2.
        """
        assert isinstance(date1, datetime.date)
        assert isinstance(date2, datetime.date)

        if date1 > date2:
            date1, date2 = date2, date1

        delta = date2 - date1

        # Weekdays
        days = (date1 + datetime.timedelta(i) for i in range(delta.days + 1))
        days = (day for day in days if day.weekday() in {0, 1, 2, 3, 4})
        days = set(days)
        # remove Bank Holidays
        bank_holidays = self.get_bank_holidays()
        days -= bank_holidays

        return days
