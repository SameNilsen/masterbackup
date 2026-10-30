import pytest


def test_add_positive():
    assert add(2, 3) == 5


def test_add_negative():
    assert add(-5, -7) == -12


def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5


def test_add_returns_int():
    assert isinstance(add(3, 4), int)


def test_add_type_error_string():
    with pytest.raises(TypeError):
        add('1', '2')


def test_add_type_error_float():
    with pytest.raises(TypeError):
        add(1.5, 2)


def test_add_type_error_none():
    with pytest.raises(TypeError):
        add(None, 2)


def add(x: int, y: int) -> int:
    """Add two numbers x and y.

    >>> add(2, 3)
    5
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both arguments must be integers")
    return x + y



METADATA = {}


def test_check():
    import random

    assert add(0, 1) == 1
    assert add(1, 0) == 1
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(7, 5) == 12

    for i in range(100):
        x, y = random.randint(0, 1000), random.randint(0, 1000)
        assert add(x, y) == x + y

