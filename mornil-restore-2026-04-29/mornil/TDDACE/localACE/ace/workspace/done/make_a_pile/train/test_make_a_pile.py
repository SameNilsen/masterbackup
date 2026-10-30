import pytest

# Helper to compute the expected pile sequence programmatically

def expected_pile(n: int) -> list[int]:
    """Return the expected stones per level for a pile of size `n`.
    The first level has `n` stones; each subsequent level increases by 2.
    """
    return [n + 2 * i for i in range(n)]

# Test that odd `n` yields an oddâindexed sequence

def test_make_a_pile_odd_sequence():
    n = 5
    result = make_a_pile(n)
    assert result == expected_pile(n)
    # Verify each level follows the rule: starts odd and increments by 2
    for i, val in enumerate(result):
        expected_val = n + 2 * i
        assert val == expected_val

# Test that even `n` yields an evenâindexed sequence

def test_make_a_pile_even_sequence():
    n = 6
    result = make_a_pile(n)
    assert result == expected_pile(n)
    # Verify parity: all values are even
    for val in result:
        assert val % 2 == 0

# Test the trivial case of a singleâlevel pile

def test_make_a_pile_single_level():
    n = 1
    assert make_a_pile(n) == [1]

# Test that the returned list has the correct length

def test_make_a_pile_length():
    for n in [1, 2, 3, 4, 10, 15]:
        result = make_a_pile(n)
        assert len(result) == n

# Verify general property: each subsequent level is two more than previous

def test_make_a_pile_increment_rule():
    n = 8
    result = make_a_pile(n)
    for i in range(1, len(result)):
        assert result[i] - result[i-1] == 2

def make_a_pile(n):
    """Return a list of the number of stones in each of the n pile levels.

    The first level contains ``n`` stones.  Every subsequent level contains
    the next odd number (if ``n`` is odd) or the next even number (if ``n`` is
    even).  This sequence is an arithmetic progression with step ``2``, so the
    element at index ``i`` equals ``n + 2*i``.

    Parameters
    ----------
    n : int
        Positive integer specifying the number of levels.

    Returns
    -------
    list[int]
        List of length ``n`` containing the stone counts for each level.

    Raises
    ------
    TypeError
        If ``n`` is not an instance of ``int``.
    ValueError
        If ``n`` is less than 1.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")
    # Arithmetic progression: start=n, step=2
    return [n + 2 * i for i in range(n)]

def test_check():

    # Check some simple cases
    assert make_a_pile(3) == [3, 5, 7], "Test 3"
    assert make_a_pile(4) == [4,6,8,10], "Test 4"
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"





