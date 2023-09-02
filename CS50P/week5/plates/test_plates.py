from plates import is_valid

def test_correct():
    assert is_valid("CS50") == True

def test_initial():
    assert is_valid("50CS") == False

def test_number():
    assert is_valid("50") == False

def test_firstnumber():
    assert is_valid("CS05") == False

def test_finalnumber():
    assert is_valid("CS50P") == False

def test_puntuaction():
    assert is_valid("PI3.14") == False

def test_minchar():
    assert is_valid("H") == False

def test_maxchar():
    assert is_valid("OUTATIME") == False