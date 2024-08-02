import pytest
from working import convert


def test_time_mins():
    assert convert("12:34 AM to 12:56 PM") == "00:34 to 12:56"
    assert convert("9:00 AM to 5:30 PM") == "09:00 to 17:30"
    assert convert("5:30 PM to 9:00 AM") == "17:30 to 09:00"


def test_time_nomins():
    assert convert("12 AM to 12 PM") == "00:00 to 12:00"
    assert convert("9 AM to 5 PM") == "09:00 to 17:00"


def test_time_valid():
    with pytest.raises(ValueError):
        convert("31:00 AM to 10:00 PM")
        convert("10:00 AM to 31:00 PM")
        convert("10:60 AM to 2:00 PM")
        convert("2:00 AM to 10:60 PM")


def test_input_format1():
    with pytest.raises(ValueError):
        convert("10AM9PM")
        convert("10:00AM2:00PM")


def test_input_format2():
    with pytest.raises(ValueError):
        convert("10:00 AM - 2:00 PM")
        convert("10:00AM - 2:00PM")
        convert("10:00 AM to2:00 PM")
        convert("10:00 AMto 2:00 PM")
        convert("10:00AMto2:00PM")
        convert("10:00AM2:00PM")
        convert("cat to dog")

