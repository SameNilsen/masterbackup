def test_add_basic_integers():
    assert add(2, 3) == 5


def test_add_two_examples():
    assert add(5, 7) == 12


def test_add_zero():
    assert add(0, 0) == 0


def test_add_negative_positive():
    assert add(-5, 3) == -2


def test_add_negative_negative():
    assert add(-5, -5) == -10


def test_add_large_values():
    assert add(1000000000, 2000000000) == 3000000000


def test_return_type():
    assert isinstance(add(2, 3), int)

def add(x: int, y: int):
    """Return the sum of two integers x and y."""
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

