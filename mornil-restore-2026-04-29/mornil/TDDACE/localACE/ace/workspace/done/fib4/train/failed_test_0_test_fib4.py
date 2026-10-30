import pytest


# ---------------------------------------------------------------
# Base case checks â verify the hardâcoded initial values.
# ---------------------------------------------------------------

def test_fib4_base_cases():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2


# ---------------------------------------------------------------
# Example values from the docstring.
# ---------------------------------------------------------------

def test_fib4_examples():
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14


# ---------------------------------------------------------------
# Known values for n = 0..14 â computed programmatically in the test
# to avoid manual mistakes (saiâ00004).
# ---------------------------------------------------------------

def _expected_fib4_sequence(limit: int) -> list[int]:
    """Return the fib4 sequence up to the given limit.
    The implementation mirrors the recurrence strictly.
    """
    seq = [0] * max(limit + 1, 5)  # Pad to handle indices 0â4
    seq[0], seq[1], seq[2], seq[3] = 0, 0, 2, 0
    for n in range(4, limit + 1):
        seq[n] = seq[n - 1] + seq[n - 2] + seq[n - 3] + seq[n - 4]
    return seq[:limit + 1]


def test_fib4_known_values():
    expected = _expected_fib4_sequence(14)
    for n, val in enumerate(expected):
        assert fib4(n) == val, f"Mismatch at n={n}: expected {val}"


# ---------------------------------------------------------------
# Type validation â nonâint arguments should raise TypeError
# ---------------------------------------------------------------

def test_fib4_type_validation():
    for invalid in ("10", 3.14, None):
        with pytest.raises(TypeError):
            fib4(invalid)


# ---------------------------------------------------------------
# Negative indices â should raise ValueError; recurrence only defined
# for n >= 0.
# ---------------------------------------------------------------

def test_fib4_negative_value():
    with pytest.raises(ValueError):
        fib4(-1)


# ---------------------------------------------------------------
# Largeân test â ensure implementation handles large inputs
# without recursion limits and returns a nonânegative integer.
# ---------------------------------------------------------------

def test_fib4_large_n_return_type():
    result = fib4(1000)
    assert isinstance(result, int)
    assert result >= 0
}
(Note: the function under test, `fib4`, is not imported; it will be supplied by the test runner.)

