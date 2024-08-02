import pytest

from jar import Jar


def test_init():
    jar = Jar()
    assert jar.capacity == 12
    jar1 = Jar(5)
    assert jar1.capacity == 5
    assert jar1.size == 0
    with pytest.raises(ValueError):
        jar = Jar(-1)

def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit():
    jar = Jar()
    assert jar.deposit(1) == 1
    assert jar.deposit(3) == 4
    with pytest.raises(ValueError):
        jar.deposit(-1)
        jar.deposit(13)

def test_withdraw():
    jar = Jar()
    assert jar.deposit(4)
    assert jar.withdraw(1) == 3
    assert jar.withdraw(1) == 2
    with pytest.raises(ValueError):
        jar.withdraw(-1)
        jar.withdraw(13)
