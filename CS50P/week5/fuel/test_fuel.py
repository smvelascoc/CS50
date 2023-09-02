from pytest import raises
from fuel import convert
from fuel import gauge

# Test convert
def test_convert():
    assert convert("1/2") == 50

def test_convert_zero_division():
    with raises(ZeroDivisionError):
        convert("0/0")

def test_convert_higher1():
    with raises(ValueError):
        convert("3/2")

def test_convert_notinteger():
    with raises(ValueError):
        convert("1.5/2")

# Test gauge
def test_gauge_full():
    assert gauge(99) == "F"

def test_gauge_empty():
    assert gauge(1) == "E"

def test_gauge():
    assert gauge(50) == "50%"