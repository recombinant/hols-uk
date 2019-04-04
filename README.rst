=======
hols-uk
=======


Given a date determine if it is a working day. Assumes:

    - Mon-Fri working week
    - UK Bank Holidays


Description
===========

Tested with Python 3.7 only.

This package uses data from https://www.gov.uk/bank-holidays for statutory
UK Bank Holidays to determine if a given date is a Bank Holiday::

    from datetime import date
    from hols_uk import Holidays

    today = datetime.date.today()
    holidays = Holidays()
    if holidays.is_bank_holiday():
        print('Today is a Bank Holiday)
    elif holidays.is_working_day():
        print('Today is a working day')
    else:
        print('Today is at the weekend')

