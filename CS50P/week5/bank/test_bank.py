from bank import value

def test_hello():
    assert value("Hello") == 0

def test_phrase():
    assert value(" Hello ") == 0

def test_phrase():
    assert value("Hello, Newman") == 0

def test_h():
    assert value("How you doing?") == 20

def test_hi():
    assert value("What's happening") == 100

def test_puntuacion():
    assert value("What's up?") == 100