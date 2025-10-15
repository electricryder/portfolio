import fuel
import pytest

def test_conversion():
    assert fuel.convert("4/4") == 100
    assert fuel.convert("1/100") == 1
    assert fuel.convert("1/2") == 50


def test_invalidfraction():
    with pytest.raises(ValueError):
        fuel.convert("5/4")


def test_dividebyzero():
    with pytest.raises(ZeroDivisionError):
        fuel.convert("4/0")


def test_gauge():
    assert fuel.gauge(99) == "F"
    assert fuel.gauge(1) == "E"
    assert fuel.gauge(25) == "25%"
