import pytest

# Helper: expected Fibonacci numbers for indices 0â10
BASE_FIB = [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]


def test_fib_zero_and_small_values():
    """Verify that fib returns the correct sequence for 0â10."""
    for idx, expected in enumerate(BASE_FIB):
        assert fib(idx) == expected,


def test_fib_large_value():
    """Check a larger index to ensure algorithm scales and holds.
    The 50th Fibonacci number is 12586269025."""
    assert fib(50) == 12586269025


def test_fib_type_validation_for_non_int():
    """fib should raise TypeError when argument is not an int."""
    with pytest.raises(TypeError):
        fib(3.14)
    with pytest.raises(TypeError):
        fib("10")


def test_fib_negative_index_raises():
    """fib should raise ValueError for a negative index."""
    with pytest.raises(ValueError):
        fib(-1)



def fib(n: int) -> int:
    """
    Return n-th Fibonacci number using an iterative approach.
    Raises TypeError if n is not an int.
    Raises ValueError if n is negative.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be non-negative")
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a



METADATA = {}


def test_check():
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(11) == 89
    assert fib(12) == 144

