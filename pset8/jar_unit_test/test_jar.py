import pytest
from jar import Jar


def test_init_default():
    jar = Jar()
    assert jar.size == 0
    assert jar.capacity == 12


def test_init_custom():
    jar = Jar(5, 3)
    assert jar.size == 3
    assert jar.capacity == 5


def test_init_improper():
    with pytest.raises(ValueError):
        jar = Jar(0)

    with pytest.raises(ValueError):
        jar = Jar(-4)

    with pytest.raises(ValueError):
        jar = Jar(0.5)

    with pytest.raises(ValueError):
        jar = Jar(12, 13)

    with pytest.raises(ValueError):
        jar = Jar(12, -1)

    with pytest.raises(ValueError):
        jar = Jar(12, 0.5)


def test_str():
    jar = Jar()
    assert str(jar) == ""
    jar.deposit(1)
    assert str(jar) == "🍪"
    jar.deposit(11)
    assert str(jar) == "🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪🍪"


def test_deposit_proper():
    jar = Jar()
    assert jar.size == 0
    jar.deposit(3)
    assert jar.size == 3
    jar.deposit(7)
    assert jar.size == 10


def test_deposit_improper():
    jar = Jar(5, 5)
    with pytest.raises(ValueError):
        jar.deposit(1)

    jar = Jar(5, 3)
    with pytest.raises(ValueError):
        jar.deposit(-1)


def test_withdraw_proper():
    jar = Jar(12, 12)
    assert jar.size == 12
    jar.withdraw(3)
    assert jar.size == 9
    jar.withdraw(7)
    assert jar.size == 2


def test_withdraw_improper():
    jar = Jar()
    with pytest.raises(ValueError):
        jar.withdraw(1)

    jar = Jar(5, 3)
    with pytest.raises(ValueError):
        jar.withdraw(-1)
