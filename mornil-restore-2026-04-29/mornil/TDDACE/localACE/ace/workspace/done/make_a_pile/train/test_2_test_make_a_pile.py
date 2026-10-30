def expected_pile(n):
    """Return the expected result of make_a_pile for a given n.
    It mirrors the rule: level i (0âbased) has n + 2*i stones.
    """
    return [n + 2 * i for i in range(n)]


def test_make_a_pile_single():
    """The function should return a list containing only the first stone count."""
    assert make_a_pile(1) == expected_pile(1)


def test_make_a_pile_basic_odd():
    """Odd n: the list should contain consecutive odd numbers starting at n."""
    assert make_a_pile(3) == expected_pile(3)


def test_make_a_pile_basic_even():
    """Even n: the list should contain consecutive even numbers starting at n."""
    assert make_a_pile(4) == expected_pile(4)


def test_make_a_pile_large_even_and_odd():
    """Test larger values for both parity to catch any offâbyâone errors."""
    assert make_a_pile(10) == expected_pile(10)
    assert make_a_pile(7)  == expected_pile(7)


def test_make_a_pile_returns_list():
    """The output should be a list, not any other iterable type."""
    result = make_a_pile(5)
    assert isinstance(result, list)


def make_a_pile(n):
    """Return a list of stone counts for each level in a pile.

    The pile has `n` levels.  Level *i* (0âbased) starts with `n`
    stones and each subsequent level increases the count by 2.
    This produces a sequence of consecutive odd numbers if `n` is odd
    and consecutive even numbers if `n` is even.

    Parameters
    ----------
    n: int
        Positive integer indicating the number of levels.  Must be
        greater than 0.

    Returns
    -------
    list[int]
        List of length `n` where element i is the number of stones in
        level i+1.

    Raises
    ------
    TypeError
        If `n` is not an integer.
    ValueError
        If `n` is not positive.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be a positive integer")

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





