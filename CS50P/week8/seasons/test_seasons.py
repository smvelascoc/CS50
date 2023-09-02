from datetime import date
from seasons import to_date
from seasons import minutes
from pytest import raises

def test_to_date_valid():
    assert to_date("1999-01-01") == date(1999,1,1)

def test_to_date_invalid_format():
    with raises(ValueError):
        to_date("1 January, 1999")

def test_to_date_invalid_date():
    with raises(ValueError):
        to_date("1999-13-01")

def test_minutes_valid():
    assert minutes(date(date.today().year - 1, date.today().month, date.today().day)) == "Five hundred twenty-five thousand, six hundred minutes"

