from twttr import shorten

def test_vocal():
    assert shorten("Twitter") == "Twttr"

def test_phrase():
    assert shorten("What's your name?") == "Wht's yr nm?"

def test_consonants():
    assert shorten ("CS50") == "CS50"

def test_vocal_mayuscula():
    assert shorten ("HELLO, WORLD") == "HLL, WRLD"