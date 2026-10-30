def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def test_add_with_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(3, 0) == 3

def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-5, -7) == -12

def test_add_mixed_sign_numbers():
    assert add(-2, 3) == 1
    assert add(5, -7) == -2

def test_add_large_numbers():
    large = 10 ** 12
    assert add(large, large) == 2 * large

def test_add_type_error():
    import pytest
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, "3")

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

