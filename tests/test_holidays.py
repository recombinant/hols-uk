#!/usr/bin/env python
# -*- coding: utf-8 -*-
import datetime

import pytest

from hols_uk.holidays import Holidays


@pytest.fixture(scope='module')
def holidays():
    return Holidays()


def test_1(holidays):
    date1 = datetime.date(2016, 3, 28)
    date2 = datetime.date(2016, 4, 7)

    days = holidays.get_working_days(date1, date2)
    assert len(days) == 8

    days = holidays.get_working_days(date2, date1)
    assert len(days) == 8


def test_2(holidays):
    assert not holidays.is_working_day(datetime.date(2016, 12, 24))
    assert not holidays.is_working_day(datetime.date(2016, 12, 25))
    assert not holidays.is_working_day(datetime.date(2016, 12, 26))
    assert not holidays.is_working_day(datetime.date(2016, 12, 27))
    assert holidays.is_working_day(datetime.date(2016, 12, 28))


def test_3(holidays):
    date1 = datetime.date(2016, 12, 30)
    date2 = datetime.date(2017, 1, 1)
    days = holidays.get_working_days(date1, date2)
    assert len(days) == 1


def test_4(holidays):
    date1 = datetime.date(2016, 12, 25)
    date2 = datetime.date(2016, 12, 26)
    days = holidays.get_working_days(date1, date2)
    assert len(days) == 0


def test_5(holidays):
    date1 = datetime.date(2016, 12, 22)
    date2 = datetime.date(2016, 12, 26)
    assert not holidays.is_bank_holiday(date1)
    assert holidays.is_bank_holiday(date2)
