def test_add_basic_positive():
    assert add(2, 3) == 5

def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_negative():
    assert add(-2, 3) == 1
    assert add(3, -5) == -2

def test_add_both_negative():
    assert add(-2, -3) == -5

def test_add_large_numbers():
    assert add(10**12, 10**12) == 2 * 10**12

def test_add_invalid_type():
    import pytest
    with pytest.raises(TypeError):
        add("1", 2)

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
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





