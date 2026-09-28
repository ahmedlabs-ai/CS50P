from fuel import convert, gauge
import pytest

def test_convert_normal():
    assert convert("3/4") == 75
    assert convert("1/2") == 50
    assert convert("1/100") == 1

def test_convert_error():
    with pytest.raises(ValueError):
        convert("5/3")
    with pytest.raises(ValueError):
        convert("1/-2")
    with pytest.raises(ValueError):
        convert("-1/2")
    with pytest.raises(ZeroDivisionError):
        convert("3/0")
    with pytest.raises(ValueError):
        convert("a/4")
    with pytest.raises(ValueError):
        convert("3/a")

def test_gauge():
    assert gauge(0) == "E"
    assert gauge(1) == "E"
    assert gauge(50) == "50%"
    assert gauge(75) == "75%"
    assert gauge(99) == "F"
    assert gauge(100) == "F"