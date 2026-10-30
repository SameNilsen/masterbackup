def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def test_add_negative_numbers():
    assert add(-1, -1) == -2
    assert add(-5, 3) == -2

def test_add_zero():
    assert add(0, 0) == 0
    assert add(5, 0) == 5
    assert add(0, 7) == 7

def test_add_large_numbers():
    assert add(10**10, 10**10) == 2 * 10**10

def add(x: int, y: int) -> int:
    """Return the sum of two integers.

    Parameters:
        x (int): First number to add.
        y (int): Second number to add.

    Returns:
        int: The sum of `x` and `y`.
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

