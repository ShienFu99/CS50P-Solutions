import pytest
from twttr import shorten


def test_shorten_default():
    with pytest.raises(TypeError):
        shorten()


def test_shorten_blank():
    assert shorten("") == ""


def test_shorten_lowercase():
    assert shorten("aeiou") == ""
    assert shorten("hello, world") == "hll, wrld"


def test_shorten_uppercase():
    assert shorten("AEIOU") == ""
    assert shorten("HELLO, WORLD") == "HLL, WRLD"


def test_shorten_num():
    assert shorten("5434") == "5434"
