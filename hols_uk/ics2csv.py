#
# -*- mode: python tab-width: 4 coding: utf-8 -*-
"""
Read the UK Government .ICS file, extract the Bank Holidays with associated
names into the "hols-uk.csv"
"""
import csv
import datetime
import re
from datetime import timedelta
from pathlib import Path


def hols2csv(holidays, csv_path):
    """
    Add the holidays to `csv_path`. Create `csv_path` if necessary.

    Args:
        holidays (dict): Holiday date vs name.
        csv_path (Path): Path to csv file.
    """
    existing_holidays = {}
    if csv_path.is_file():
        with csv_path.open('rt', encoding='utf-8', newline='') as fs:
            rows = csv.DictReader(fs, dialect='excel')
            existing_holidays = {
                datetime.datetime.strptime(row['Date'], '%d-%b-%Y').date():
                    row['Name'] for row in rows}

    existing_holidays.update(holidays)
    days = list(existing_holidays)
    days.sort()

    # Prevent US / UK month day confusion, use abbreviated month.
    # e.g. 24-Dec-2015
    with csv_path.open('wt', encoding='utf-8', newline='') as fs:
        writer = csv.writer(fs)
        writer.writerow(['Date', 'Name'])
        for day in days:
            writer.writerow([day.strftime('%d-%b-%Y'), existing_holidays[day]])


def import_ics(ics_path):
    """
    Import the .ics file holding the UK Bank holidays.

    This is available from:
        https://www.gov.uk/bank-holidays

    Returns:
        dict: Holiday date vs name.
    """
    holidays = dict()

    ro_start = re.compile(r'DTSTART;VALUE=DATE:([0-9]{4})([0-9]{2})([0-9]{2})')
    ro_end = re.compile(r'DTEND;VALUE=DATE:([0-9]{4})([0-9]{2})([0-9]{2})')
    ro_summary = re.compile(r'SUMMARY:(.*)')

    ro_trigger = re.compile(r'END:VEVENT')

    start_date = end_date = summary = None

    lines = ics_path \
        .open('rt', encoding='UTF-8') \
        .read() \
        .splitlines(keepends=False)

    for line in lines:
        if start_date is None:
            m = ro_start.match(line)
            if m:
                year, month, day = list(map(int, m.groups()))
                start_date = datetime.date(year, month, day)
        if end_date is None:
            m = ro_end.match(line)
            if m:
                year, month, day = list(map(int, m.groups()))
                end_date = datetime.date(year, month, day)
        if summary is None:
            m = ro_summary.match(line)
            if m:
                summary = m.group(1)

        if ro_trigger.match(line):
            assert start_date is not None
            assert end_date is not None

            d = start_date
            while d < end_date:
                holidays[d] = summary or ''
                d += timedelta(days=1)

            start_date = end_date = summary = None

    return holidays


def main():
    holidays = dict()
    files = Path(__file__).parent.glob('*.ics')
    for f in files:
        holidays.update(import_ics(f))

    csv_path = Path(__file__).parent / 'hols-uk.csv'
    hols2csv(holidays, csv_path)


if __name__ == '__main__':
    main()
