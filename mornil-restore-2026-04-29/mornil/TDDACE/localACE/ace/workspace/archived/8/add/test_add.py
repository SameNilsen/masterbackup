import random
import pytest


def test_add_basic():
    assert add(2, 3) == 5
    assert add(5, 7) == 12


def test_add_zero_and_negative():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(-5, 5) == 0


def test_add_commutativity():
    for _ in range(100):
        a = random.randint(-1000, 1000)
        b = random.randint(-1000, 1000)
        assert add(a, b) == add(b, a)


def test_add_large_numbers():
    large1 = 10**15
    large2 = 10**15 + 123456
    assert add(large1, large2) == large1 + large2


def test_add_type_error():
    with pytest.raises(TypeError):
        add('1', 2)


def add(x: int, y: int):
    """Add two numbers x and y

    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
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

