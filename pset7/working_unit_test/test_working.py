from working import convert, convert_time_period
import pytest


def test_convert_default():
    with pytest.raises(TypeError):
        convert()


def test_convert_blank():
    with pytest.raises(ValueError):
        convert("")


def test_convert_improper_string():
    with pytest.raises(ValueError):
        convert("5 to 7")
        convert("5 AM TO 7 PM")
        convert("5 am to 7 pm")
        convert("5 A.M. to 7 P.M.")


def test_convert_hours():
    convert("12 AM to 12 PM") == "00:00 to 12:00"
    convert("1 PM to 1 AM") == "13:00 to 01:00"


def test_convert_mixed_times():
    convert("5 AM to 7:30 PM") == "05:00 to 19:30"
    convert("3:27 PM to 4 AM") == "15:27 to 04:00"


def test_convert_hours_and_minutes():
    convert("5:00 AM to 7:59 AM") == "05:00 to 07:59"
    convert("3:43 PM to 11:37 AM") == "15:43 to 11:37"


def test_convert_invalid_hours():
    with pytest.raises(ValueError):
        convert("0 AM to 0:00 PM")
        convert("13 PM to 11:37 AM")


def test_convert_invalid_minutes():
    with pytest.raises(ValueError):
        convert("4:-01 AM to 5:00 PM")
        convert("12:60 PM to 11:37 AM")


def test_convert_time_period_default():
    with pytest.raises(TypeError):
        convert_time_period()


def test_convert_time_period_blank():
    with pytest.raises(TypeError):
        convert_time_period("", "")


def test_convert_time_period_invalid_hours():
    with pytest.raises(ValueError):
        convert_time_period(13, "AM")
        convert_time_period(0, "PM")


def test_convert_time_period_proper():
    convert_time_period(12, "AM") == 0
    convert_time_period(12, "PM") == 12
    convert_time_period(1, "AM") == 1
    convert_time_period(1, "PM") == 13
