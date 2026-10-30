def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_negative_numbers():
    assert add(-1, -2) == -3
    assert add(-5, 5) == 0
    assert add(3, -7) == -4

def test_add_large_numbers():
    large_a = 10**20
    large_b = 10**15
    assert add(large_a, large_b) == large_a + large_b
    assert add(-large_a, large_b) == -large_a + large_b

def test_add_docstring_examples():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def add(x: int, y: int) -> int:
    """Add two numbers x and y.
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

