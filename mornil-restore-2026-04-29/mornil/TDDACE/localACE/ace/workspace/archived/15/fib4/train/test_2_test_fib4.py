import pytest

# ---------------------------------------------------------------------------
# Parametrised test for known values of fib4.  Includes the base cases and
# several values derived from the recurrence.
# ---------------------------------------------------------------------------
@pytest.mark.parametrize(
    "n,expected",
    [
        (0, 0),
        (1, 0),
        (2, 2),
        (3, 0),
        (4, 2),
        (5, 4),
        (6, 8),
        (7, 14),
        (8, 28),
        (9, 54),
        (10, 104),
        # A larger value to ensure the recurrence works beyond the base cases
        (20, 73552),
    ],
)
def test_fib4_known_values(n, expected):
    assert fib4(n) == expected

# ---------------------------------------------------------------------------
# Tests for error handling â negative indices should raise ValueError.
# ---------------------------------------------------------------------------
def test_fib4_negative_index_raises_value_error():
    with pytest.raises(ValueError):
        fib4(-1)

# ---------------------------------------------------------------------------
# Tests for type safety â nonâint arguments should raise TypeError.
# ---------------------------------------------------------------------------
def test_fib4_invalid_type_string_raises_type_error():
    with pytest.raises(TypeError):
        fib4("10")

def test_fib4_invalid_type_float_raises_type_error():
    with pytest.raises(TypeError):
        fib4(10.5)

# ---------------------------------------------------------------------------
# Verify the function always returns an integer.
# ---------------------------------------------------------------------------
def test_fib4_return_type_is_int():
    assert isinstance(fib4(5), int)


def fib4(n: int) -> int:
    """Return the nâth element of the Fib4 sequence.

    The sequence is defined
    fib4(0) = 0, fib4(1) = 0, fib4(2) = 2, fib4(3) = 0
    and for n >= 4
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4).

    Parameters
    ----------
    n: int
        the index in the sequence (must be nonânegative)

    Returns
    -------
    int
        the Fib4 value at position n
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be nonânegative")

    # Base values
    base = [0, 0, 2, 0]
    if n < 4:
        return base[n]

    seq = base.copy()
    for i in range(4, n + 1):
        seq.append(seq[-1] + seq[-2] + seq[-3] + seq[-4])
    return seq[n]



METADATA = {}


def test_check():
    assert fib4(5) == 4
    assert fib4(8) == 28
    assert fib4(10) == 104
    assert fib4(12) == 386

