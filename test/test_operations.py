from src.math_operations import add, sub

def test_add():
    assert add(5+2) == 7
    assert add(5+5) == 10
    assert add(4+4) == 8


def test_sub():
    assert sub(-1,1) == -2
    assert sub(7,3) == 4
    assert sub(6,3) == 3
    assert sub(9,3) == 6