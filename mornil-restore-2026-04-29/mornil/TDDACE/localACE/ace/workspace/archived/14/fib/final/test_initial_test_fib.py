import pytest


def test_fibonacci_values():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(10) == 55
    assert fib(20) == 6765

@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
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
    ],
)
def test_fibonacci_param(n, expected):
    assert fib(n) == expected


def test_result_type():
    assert isinstance(fib(10), int)


def test_fibonacci_idempotent():
    for n in range(20):
        assert fib(n) == fib(n)

def fib(n: int):
    """Return n-th Fibonacci number.

    The Fibonacci sequence is defined as:
    fib(0) = 0
    fib(1) = 1
    fib(n) = fib(n-1) + fib(n-2) for n > 1

    Parameters
    ----------
    n : int
        Index in the Fibonacci sequence (nonânegative).

    Returns
    -------
    int
        The n-th Fibonacci number.

    Examples
    --------
    >>> fib(0)
    0
    >>> fib(1)
    1
    >>> fib(8)
    21
    >>> fib(10)
    55
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be nonânegative")
    if n == 0:
        return 0
    if n == 1:
        return 1
    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



METADATA = {}


def test_check():
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(11) == 89
    assert fib(12) == 144

