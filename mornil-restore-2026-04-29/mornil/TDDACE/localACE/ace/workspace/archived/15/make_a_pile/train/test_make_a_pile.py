def test_make_a_pile_basic():
    assert make_a_pile(1) == [1]
    assert make_a_pile(2) == [2, 4]
    assert make_a_pile(3) == [3, 5, 7]

def test_make_a_pile_increment_by_2():
    for n in range(1, 10):
        result = make_a_pile(n)
        assert len(result) == n
        for i in range(n - 1):
            assert result[i + 1] - result[i] == 2

def test_make_a_pile_parity():
    for n in [1, 2, 5, 6]:
        result = make_a_pile(n)
        expected_parity = n % 2
        for val in result:
            assert val % 2 == expected_parity

def test_make_a_pile_independence():
    a = make_a_pile(4)
    b = make_a_pile(4)
    a[0] = -999
    assert b[0] == 4

def test_make_a_pile_large():
    n = 1000
    result = make_a_pile(n)
    assert result[0] == n
    assert result[-1] == n + 2 * (n - 1)
    assert len(result) == n
    for i in [5, 200, 500, 999]:
        assert result[i] == n + 2 * i

def make_a_pile(n: int) -> list[int]:
    """Return a pile of stones for a given positive integer *n*.

    The pile consists of *n* levels.  The first level contains *n* stones, and each
    subsequent level contains two stones more than the previous one, preserving
    the parity of *n*.

    Parameters
    ----------
    n : int
        The number of levels (and the number of stones in the first level).

    Returns
    -------
    list[int]
        A list of length *n* where element *i* (0âbased) equals ``n + 2*i``.

    Raises
    ------
    TypeError
        If *n* is not an instance of ``int``.
    ValueError
        If *n* is not positive.
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

