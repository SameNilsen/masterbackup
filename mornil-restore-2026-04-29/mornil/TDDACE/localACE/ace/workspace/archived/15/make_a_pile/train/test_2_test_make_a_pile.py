def test_make_a_pile_small_odd():
    assert make_a_pile(1) == [1]
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(5) == [5, 7, 9, 11, 13]

def test_make_a_pile_small_even():
    assert make_a_pile(2) == [2, 4]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(6) == [6, 8, 10, 12, 14, 16]

def test_make_a_pile_parity_and_step():
    for n in range(1, 11):
        pile = make_a_pile(n)
        assert len(pile) == n
        parity = n % 2
        assert all(p % 2 == parity for p in pile)
        if len(pile) > 1:
            assert all(pile[i+1] - pile[i] == 2 for i in range(n-1))

def make_a_pile(n: int) -> list[int]:
    """Return a list of stone counts for a pile of n levels.
    Each level contains the same parity as the first level and increases by 2.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n <= 0:
        raise ValueError("n must be positive")
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

