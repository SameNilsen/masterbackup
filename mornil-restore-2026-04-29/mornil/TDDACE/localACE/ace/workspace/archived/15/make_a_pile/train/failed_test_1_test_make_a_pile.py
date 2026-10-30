import pytest


def test_make_a_pile_valid_cases():
    """Verify expected outputs for typical positive integer inputs."""
    assert make_a_pile(3) == [3, 5, 7]
    assert make_a_pile(4) == [4, 6, 8, 10]
    assert make_a_pile(1) == [1]
    assert make_a_pile(2) == [2, 4]


def test_make_a_pile_sequence_parity():
    """Ensure the sequence length equals `n` and that all numbers preserve the input parity."""
    n = 5
    pile_odd = make_a_pile(n)
    assert len(pile_odd) == n
    assert all(x % 2 == 1 for x in pile_odd)  # all odd numbers

    n_even = 6
    pile_even = make_a_pile(n_even)
    assert len(pile_even) == n_even
    assert all(x % 2 == 0 for x in pile_even)  # all even numbers


def test_make_a_pile_invalid_inputs():
    """Verify that nonâpositive integers and nonâint types raise appropriate errors."""
    with pytest.raises(ValueError):
        make_a_pile(0)
    with pytest.raises(ValueError):
        make_a_pile(-3)

    with pytest.raises(TypeError):
        make_a_pile(3.5)
    with pytest.raises(TypeError):
        make_a_pile("5")


