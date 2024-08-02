import pytest
from fuel import convert,gauge

def test_value_error():
    with pytest.raises(ValueError):
        convert("cat/dog")

def test_zerodivision_error():
    with pytest.raises(ZeroDivisionError):
        convert("1/0")

def test_convert():
    assert convert("2/5") == 40

def test_gauge_E():
    assert gauge(1) == "E"
    assert gauge(0) == "E"

def test_gauge_F():
    assert gauge(99) == "F"
    assert gauge(100) == "F"

def test_print():
    assert gauge(75) == "75%"
