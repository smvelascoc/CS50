from um import count

def test_count1():
    assert count("um") == 1

def test_count_symbol():
    assert count("um?") == 1

def test_case_sensitive():
    assert count("Um, thanks for the album") == 1

def test_no_count():
    assert count("Yummy") == 0