"import pytest


def test_balanced_and_weight_within():
    assert will_it_fly([1, 2, 1], 5) is True


def test_balanced_but_weight_exceeds():
    assert will_it_fly([1, 2, 1], 3) is False


def test_unbalanced_but_weight_within():
    assert will_it_fly([1, 2, 3], 10) is False


def test_single_element_balanced():
    assert will_it_fly([5], 5) is True


def test_empty_list_with_positive_weight():
    assert will_it_fly([], 10) is True


def test_empty_list_with_negative_weight():
    assert will_it_fly([], -1) is False


def test_negative_elements_balanced_with_negative_weight_equal():
    assert will_it_fly([-1, -2, -1], -4) is True


def test_negative_elements_balanced_with_higher_negative_weight():
    assert will_it_fly([-1, -2, -1], -3) is True


def test_negative_elements_balanced_with_lower_negative_weight():
    assert will_it_fly([-1, -2, -1], -5) is False


def test_zero_weight_with_zero_sum():
    assert will_it_fly([0, 0, 0], 0) is True
"

def will_it_fly(q: list[int], w: int) -> bool:
    """Return True iff *q* is a palindrome and its sum is at most *w*.

    Parameters
    ----------
    q : list[int]
        The sequence of elements to evaluate.
    w : int
        The maximum allowable weight.

    Returns
    -------
    bool
        ``True`` when the list is balanced (palindromic) and its total weight
        does not exceed ``w``; otherwise ``False``.
    """
    return q == q[::-1] and sum(q) <= w

def test_check():

    # Check some simple cases
    assert will_it_fly([3, 2, 3], 9) is True
    assert will_it_fly([1, 2], 5) is False
    assert will_it_fly([3], 5) is True
    assert will_it_fly([3, 2, 3], 1) is False


    # Check some edge cases that are easy to work out by hand.
    assert will_it_fly([1, 2, 3], 6) is False
    assert will_it_fly([5], 5) is True

