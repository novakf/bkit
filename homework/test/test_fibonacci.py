import pytest, sys
from fibonacci import fibonacci


def test_fibonacci():
    res = [1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
    assert list(fibonacci(10)) == res        

def test_negative():
    assert list(fibonacci(-1)) == []

def test_lazy():
    assert sys.getsizeof(fibonacci(10)) == sys.getsizeof(fibonacci(10_000))  
    


