import pytest
from bank import value


def test_value_default():
    with pytest.raises(TypeError):
        value()


def test_value_blank():
    assert value("") == 100


def test_value_hello():
    assert value("hello") == 0
    assert value("HELlO, wORld") == 0


def test_value_starts_with_h():
    assert value("Hi") == 20
    assert value("h, hello") == 20


def test_value_incorrect():
    assert value("are, h hello") == 100
