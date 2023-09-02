from week7.working.working import convert
from pytest import raises

def test_correct_long():
    assert convert("9:00 AM to 5:00 PM") == ("09:00 to 17:00")

def test_correct_short():
    assert convert("9 AM to 5 PM") == ("09:00 to 17:00")

def test_mix():
    assert convert("9 AM to 5:30 PM") == ("09:00 to 17:30")

def test_midnight():
    assert convert("12:00 PM to 12:00 AM") == ("12:00 to 00:00")

def test_minutes():
    assert convert("9:30 AM to 5:30 PM") == ("09:30 to 17:30")

def test_wrong_hour():
    with raises(ValueError):
        convert("13:00 PM to 3:00 PM")

def test_wrong_minutes():
    with raises(ValueError):
        convert("5:60 AM to 3:00 PM")

def test_wrong_sep():
    with raises(ValueError):
        convert("9:00 AM - 5:00 PM")

def test_wrong_format():
    with raises(ValueError):
        convert("9:00 MM to 5:00 PM")