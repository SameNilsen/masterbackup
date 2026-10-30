import pytest
from fib4 import fib4


def test_fib4_base_cases():
    """Verify the defined base cases for n = 0..3."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_known_values():
    """Test a selection of known values beyond the base cases."""
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14
    assert fib4(8) == 28
    assert fib4(9) == 54
    assert fib4(10) == 104


def test_fib4_recurrence():
    """Confirm that the recurrence fib4(n)=sum of the previous four holds."""
    seq = [fib4(i) for i in range(11)]  # preâcompute for indices 0..10
    for i in range(4, 11):
        expected = seq[i-1] + seq[i-2] + seq[i-3] + seq[i-4]
        assert seq[i] == expected, f"Failed at n={i}: expected {expected}, got {seq[i]}"


def test_fib4_non_negative_property():
    """All results for n â¥ 0 must be nonânegative."""
    for n in range(0, 20):
        assert fib4(n) >= 0, f"Negative result for n={n}"


def test_fib4_negative_input():
    """fib4 should raise ValueError for any negative argument."""
    with pytest.raises(ValueError):
        fib4(-1)


def fib4(n: int) -> int:
    """Return the nâth Fib4 number.

    The Fib4 sequence is defined as:
    * fib4(0) = 0
    * fib4(1) = 0
    * fib4(2) = 2
    * fib4(3) = 0
    * for n â¥ 4: fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)

    The function validates that *n* is nonânegative and then uses an iterative
    slidingâwindow approach to compute the result in O(n) time and O(1) memory.
    """
    if n < 0:
        raise ValueError("n must be nonânegative")

    # Base cases
    if n == 0 or n == 1 or n == 3:
        return 0
    if n == 2:
        return 2

    # Sliding window for fib4(0), fib4(1), fib4(2), fib4(3)
    a0, a1, a2, a3 = 0, 0, 2, 0
    for _ in range(4, n + 1):
        next_val = a0 + a1 + a2 + a3
        a0, a1, a2, a3 = a1, a2, a3, next_val
    return a3



METADATA = {}


def test_check():
    assert fib4(5) == 4
    assert fib4(8) == 28
    assert fib4(10) == 104
    assert fib4(12) == 386

