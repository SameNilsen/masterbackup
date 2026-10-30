import pytest

# Parametrized test cases for the add function
@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 3, 5),
        (5, 7, 12),
        (-5, -10, -15),
        (0, 5, 5),
        (10 ** 10, 10 ** 10, 2 * 10 ** 10),
    ],
)
def test_add(x, y, expected):
    """Verify that add returns the correct sum for various integer inputs."""
    assert add(x, y) == expected


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

