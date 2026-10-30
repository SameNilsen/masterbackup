def test_make_a_pile_basic_odd():
    assert make_a_pile(3) == [3, 5, 7]


def test_make_a_pile_basic_even():
    assert make_a_pile(4) == [4, 6, 8, 10]


def test_make_a_pile_single():
    assert make_a_pile(1) == [1]


def test_make_a_pile_length_matches():
    for n in [2, 5, 10]:
        pile = make_a_pile(n)
        assert len(pile) == n, f"Expected length {n}, got {len(pile)}"


def test_make_a_pile_increment_by_two():
    n = 6
    pile = make_a_pile(n)
    for i in range(1, n):
        assert pile[i] - pile[i-1] == 2, f"Difference at index {i} not 2"


def test_make_a_pile_parity():
    pile_odd = make_a_pile(7)
    assert all(x % 2 == 1 for x in pile_odd), "Not all odd for odd n"
    pile_even = make_a_pile(8)
    assert all(x % 2 == 0 for x in pile_even), "Not all even for even n"


def test_make_a_pile_raises_value_error():
    try:
        make_a_pile(-5)
        assert False, "Expected ValueError for negative n"
    except ValueError:
        pass
    try:
        make_a_pile(0)
        assert False, "Expected ValueError for n=0"
    except ValueError:
        pass

def make_a_pile(n: int) -> list[int]:
    """Return a list of stones for each level.

    Parameters
    ----------
    n : int
        The number of levels.  Must be a positive integer.

    Returns
    -------
    List[int]
        ``n`` stones in the first level and each following level
        increases by two, preserving the parity of ``n``.

    Raises
    ------
    ValueError
        If ``n`` is not a positive integer.
    """
    if n <= 0:
        raise ValueError("n must be a positive integer")

    return [n + 2 * k for k in range(n)]


def test_check():

    # Check some simple cases
    assert make_a_pile(3) == [3, 5, 7], "Test 3"
    assert make_a_pile(4) == [4,6,8,10], "Test 4"
    assert make_a_pile(5) == [5, 7, 9, 11, 13]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]
    assert make_a_pile(8) == [8, 10, 12, 14, 16, 18, 20, 22]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

