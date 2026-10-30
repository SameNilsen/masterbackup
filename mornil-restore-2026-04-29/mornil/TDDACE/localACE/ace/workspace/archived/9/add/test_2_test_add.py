def test_add_basic():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def test_add_with_zero():
    assert add(0, 10) == 10
    assert add(10, 0) == 10

def test_add_with_negative():
    assert add(-5, 5) == 0
    assert add(-3, -4) == -7

def test_add_commutative():
    a, b = 123, 456
    assert add(a, b) == add(b, a)

def test_add_large_numbers():
    large = 10 ** 12
    assert add(large, large) == 2 * large
    assert isinstance(add(large, large), int)


def add(x: int, y: int) -> int:
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

