from numb3rs import validate

def test_good():
    assert validate("1.2.3.4") == True

def test_letters():
    assert validate("Hello") == False

def test_outrange1():
    assert validate("275.3.6.28") == False

def test_outrange2():
    assert validate("255.273.6.28") == False

def test_outrange3():
    assert validate("255.233.366.28") == False

def test_outrange4():
    assert validate("225.3.6.1000") == False

def test_lessnumbers():
    assert validate("1.2.3") == False

def test_plusnumbers():
    assert validate("1.2.3.4.5") == False

def test_min():
    assert validate("0.0.0.0") == True

def test_max():
    assert validate("255.255.255.255") == True