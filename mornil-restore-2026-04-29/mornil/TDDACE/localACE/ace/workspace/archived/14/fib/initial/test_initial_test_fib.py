import pytest

@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 3),
        (5, 5),
        (6, 8),
        (7, 13),
        (8, 21),
        (9, 34),
        (10, 55),
        (20, 6765),
        (30, 832040),
    ],
)
def test_fib_known_values(n, expected):
    assert fib(n) == expected


def test_fib_returns_int():
    assert isinstance(fib(10), int)


def test_fib_invalid_input():
    with pytest.raises(ValueError):
        fib(0)
    with pytest.raises(ValueError):
        fib(-5)

def fib(n: int):
    if not isinstance(n, int) or n <= 0:
        raise ValueError('n must be a positive integer')
    if n == 1 or n == 2:
        return 1
    a, b = 1, 1
    for _ in range(3, n + 1):
        a, b = b, a + b
    return b



METADATA = {}


def test_check():
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(11) == 89
    assert fib(12) == 144

