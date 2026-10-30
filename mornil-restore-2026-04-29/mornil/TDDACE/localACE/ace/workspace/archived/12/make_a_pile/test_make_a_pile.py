def test_make_a_pile_basic_output():
    """Verify the function produces the expected sequences for small values."""
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(1) == [1]
    assert make_a_pile(2) == [2, 4]


def test_make_a_pile_properties():
    """Check general properties across a range of inputs."""
    for n in [1, 2, 3, 4, 5, 10, 20]:
        pile = make_a_pile(n)

        # Correct length
        assert isinstance(pile, list)
        assert len(pile) == n

        # Correct parity: all elements match parity of n
        expected_parity = n % 2  # 1 for odd, 0 for even
        for v in pile:
            assert v % 2 == expected_parity

        # Successive elements differ by exactly 2
        for a, b in zip(pile, pile[1:]):
            assert b - a == 2


def make_a_pile(n: int) -> list[int]:
    """Return a list describing a pile of stones.

    Parameters
    ----------
    n : int
        The number of levels (must be a positive integer).

    Returns
    -------
    list[int]
        A list of length ``n`` where the first element is ``n`` and each subsequent
        element is 2 greater than the previous one, preserving the parity of ``n``.

    Raises
    ------
    ValueError
        If ``n`` is not a positive integer.
    """
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

