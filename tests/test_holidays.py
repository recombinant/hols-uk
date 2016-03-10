#!/usr/bin/env python
# -*- coding: utf-8 -*-
import pytest
import datetime

from hols_uk import Holidays


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

    assert not holidays.is_working_day(datetime.date(2016, 12, 24))
    assert not holidays.is_working_day(datetime.date(2016, 12, 25))
    assert not holidays.is_working_day(datetime.date(2016, 12, 26))
    assert not holidays.is_working_day(datetime.date(2016, 12, 27))
    assert holidays.is_working_day(datetime.date(2016, 12, 28))

    date1 = datetime.date(2017, 1, 1)
    date2 = datetime.date(2016, 12, 30)
    days = holidays.get_working_days(date2, date1)
    assert len(days) == 1
