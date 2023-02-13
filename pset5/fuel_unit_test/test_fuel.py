import pytest
from fuel import convert, gauge


def test_convert_default():
    with pytest.raises(TypeError):
        convert()


def test_convert_blank():
    with pytest.raises(ValueError):
        convert("")


def test_convert_invalid_format():
    with pytest.raises(ValueError):
        convert("2 over 3")
        convert("2 /3")
        conver("2/3/")


def test_convert_denominator_zero():
    with pytest.raises(ValueError):
        convert("2/0")


def test_convert_negative_numerator():
    with pytest.raises(ValueError):
        convert("-2/3")


def test_convert_numerator_zero():
    with pytest.raises(ValueError):
        convert("2/-3")


def test_convert_numerator_exceeds_denominator():
    with pytest.raises(ValueError):
        convert("5/4")


def test_convert_float():
    with pytest.raises(ValueError):
        convert("2.5/3")


def test_convert_proper():
    assert convert("2/3") == 67
    assert convert("5/200") == 3
    assert convert("7/200") == 4
    assert convert("154/1000") == 15


def test_gauge_default():
    with pytest.raises(TypeError):
        gauge()


def test_gauge_blank():
    with pytest.raises(TypeError):
        gauge()


def test_gauge_empty():
    assert gauge(0) == "E"
    assert gauge(1) == "E"


def test_gauge_full():
    assert gauge(99) == "F"
    assert gauge(100) == "F"


def test_gauge_normal():
    assert gauge(25) == "25%"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
