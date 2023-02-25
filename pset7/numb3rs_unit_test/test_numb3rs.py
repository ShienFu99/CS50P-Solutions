import pytest
from numb3rs import validate


def test_validate_default():
    with pytest.raises(TypeError):
            validate()


def test_validate_blank():
    assert validate("") == False


def test_validate_missing_num():
    assert validate("1") == False
    assert validate("2.3.4") == False


def test_validate_missing_dot():
    assert validate("1 2.3.4") == False
    assert validate("2.3.45") == False


def test_validate_negative():
    assert validate("-1.-1.-1.-1") == False


def test_validate_exceed():
    assert validate("256.245.243.13") == False


def test_validate_word():
    assert validate("cat") == False


def test_validate_proper():
    assert validate("0.0.0.0") == True
    assert validate("255.255.255.255") == True
    assert validate("127.0.0.1") == True
