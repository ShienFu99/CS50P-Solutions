#Assume all user input will be in uppercase

import pytest
from plates import is_valid


def test_is_valid_default():
    with pytest.raises(TypeError):
        is_valid()


def test_is_valid_default():
    assert is_valid("") == False


def test_is_valid_short():
    assert is_valid("A") == False


def test_is_valid_long():
    assert is_valid("AER2342") == False
    assert is_valid("AERAERA") == False


def test_is_valid_starts_not_letters():
    assert is_valid("A234") == False
    assert is_valid("234") == False


def test_is_valid_letter_after_number():
    assert is_valid("AE23A") == False


def test_is_valid_contains_spaces():
    assert is_valid("AE23 ") == False
    assert is_valid("AE2 3") == False


def test_is_valid_contains_symbols():
    assert is_valid("AE23.") == False
    assert is_valid("AE23,") == False
    assert is_valid("AE23!") == False


def test_is_valid_first_num_zero():
    assert is_valid("AE023") == False
    assert is_valid("AE0") == False


def test_is_valid_proper():
    assert is_valid("AE2344") == True
    assert is_valid("AE") == True
    assert is_valid("AERTER") == True
    assert is_valid("AERAR2") == True
