from jar import Jar
from pytest import raises

def test_init():
    jar = Jar()
    assert jar.capacity == 12

    jar2 = Jar(1)
    assert jar2.capacity == 1

    jar3 = Jar(size=2)
    assert str(jar3) == "🍪🍪"

    with raises(ValueError):
        Jar(-1)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    jar.deposit(1)
    assert str(jar) == "🍪"

def test_withdraw():
    jar = Jar(size=3)
    jar.withdraw(2)
    assert str(jar) == "🍪"