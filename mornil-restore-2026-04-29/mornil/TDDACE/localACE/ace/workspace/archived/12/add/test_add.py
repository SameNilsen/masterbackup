import pytest

# Parameterized tests for various integer combinations
@pytest.mark.parametrize(
    "x, y, expected",
    [
        (2, 3, 5),           # basic positive numbers
        (5, 7, 12),          # second example from docstring
        (-1, -2, -3),        # negative numbers
        (0, 5, 5),           # zero with positive
        (-3, 4, 1),          # mixed signs
        (999999999999, 111111111111, 1111111111110),  # large integers
    ],
)
def test_add(x, y, expected):
    result = add(x, y)
    assert result == expected
    assert isinstance(result, int)






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

def add(x: int, y: int) -> int:
    return x + y

