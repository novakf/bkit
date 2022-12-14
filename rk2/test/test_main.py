import pytest
from main import *
from main import task1, task2, task3, one_to_many, many_to_many

def test_task1():
    res = task1(one_to_many)
    expected = {'Applications':['mario.exe']}
    assert res == expected

def test_task2():
    res = task2(one_to_many)
    expected = [('Applications', 5000), ('Pictures', 8), ('Downloads', 3)]
    assert res == expected


def test_task3():
    res = task3(one_to_many)
    expected = [('mario.exe', 5000, 'Applications'), 
                ('word-download.txt', 3, 'Downloads'), 
                ('alps.png', 7, 'Pictures'), 
                ('mount.jpg', 8, 'Pictures'), 
                ('tree.jpg', 6, 'Pictures')]
    assert res == expected

