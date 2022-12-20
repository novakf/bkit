import pytest, sys
from lab1 import get_roots, get_coef


def test_get_roots():
    assert get_roots(1, -10, 9) == [-3.0, -1.0, 1.0, 3.0]
    assert get_roots(1, -2, 1) == [-1.0, 1.0]
    assert get_roots(1, 2, 3) == []

def test_get_coef():
    assert get_coef(1, "Write number 1") == 1

def test_type():
    try: 
        get_roots(12, "B", 4)
        assert False
    except TypeError:
        assert True
    


