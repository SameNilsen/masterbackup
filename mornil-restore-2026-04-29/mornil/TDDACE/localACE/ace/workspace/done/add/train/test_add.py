import pytest

def expected_add(x, y):
    return x + y

# Test normal positive integers
def test_add_basic():
    assert add(2, 3) == expected_add(2, 3)
    assert add(5, 7) == expected_add(5, 7)

# Test addition with negative numbers
def test_add_negative_numbers():
    assert add(-4, 7) == expected_add(-4, 7)
    assert add(-10, -20) == expected_add(-10, -20)

# Test addition involving zero
def test_add_zero():
    assert add(0, 0) == expected_add(0, 0)
    assert add(0, 42) == expected_add(0, 42)

# Test with very large integers
def test_add_large_numbers():
    big1 = 10**12
    big2 = 10**12
    assert add(big1, big2) == expected_add(big1, big2)

# Verify that adding a non-integer raises a TypeError
def test_add_type_mismatch():
    with pytest.raises(TypeError):
        add('a', 1)

def add(x: int, y: int):
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
    """
    if not isinstance(x, int) or not isinstance(y, int):
        raise TypeError("Both operands must be integers")
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





