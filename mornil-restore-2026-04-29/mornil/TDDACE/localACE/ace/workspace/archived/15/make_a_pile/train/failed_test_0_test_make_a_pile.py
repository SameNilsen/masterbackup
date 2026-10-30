def test_make_a_pile_basic():
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(1) == [1]
    assert make_a_pile(2) == [2, 4]


def test_make_a_pile_sequence_parity():
    pile_odd = make_a_pile(5)
    assert pile_odd == [5, 7, 9, 11, 13]
    assert all(x % 2 == 1 for x in pile_odd)

    pile_even = make_a_pile(6)
    assert pile_even == [6, 8, 10, 12, 14, 16]
    assert all(x % 2 == 0 for x in pile_even)


def test_make_a_pile_invalid_n():
    import pytest
    with pytest.raises(ValueError):
        make_a_pile(0)
    with pytest.raises(ValueError):
        make_a_pile(-3)


def test_make_a_pile_non_int_inputs():
    import pytest
    for bad in ('3', 3.0, [3], None):
        with pytest.raises(TypeError):
            make_a_pile(bad)


def test_make_a_pile_large_n():
    n = 1000
    pile = make_a_pile(n)
    assert len(pile) == n
    assert pile[0] == n
    assert pile[-1] == n + 2 * (n - 1)
    assert all(pile[i] == n + 2 * i for i in range(n))

