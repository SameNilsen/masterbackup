import pytest

# ---- Basic examples (docstring examples) ----

def test_fib_examples():
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21

# ---- Base cases and small values ----

def test_fib_base_cases():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(3) == 2
    assert fib(5) == 5

# ---- Recurrence property (for a few middle indices) ----

def test_fib_recursion_property():
    n = 12
    assert fib(n) == fib(n-1) + fib(n-2)

# ---- Verify correctness for larger indices ----

def test_fib_large_numbers():
    assert fib(50) == 12586269025
    assert fib(90) == 2880067194370816120

# ---- Error handling: negative inputs ----

def test_fib_negative_input():
    with pytest.raises(ValueError):
        fib(-5)

# ---- Error handling: wrong type ----

def test_fib_non_integer_input():
    with pytest.raises(TypeError):
        fib("10")


def fib(n: int):
    """Return the n-th Fibonacci number.

    Raises:
        TypeError: If ``n`` is not an integer.
        ValueError: If ``n`` is negative.
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

