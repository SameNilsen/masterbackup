import pytest

# Helper that implements the specification logic programmatically
# This verifies that the test expectations are correct and not based on manual counting.
def _expected(q, w):
    return (q == q[::-1]) and (sum(q) <= w)

# Sample cases provided in the problem statement

def test_will_it_fly_examples():
    assert will_it_fly([1, 2], 5) == _expected([1, 2], 5)
    assert will_it_fly([3, 2, 3], 1) == _expected([3, 2, 3], 1)
    assert will_it_fly([3, 2, 3], 9) == _expected([3, 2, 3], 9)
    assert will_it_fly([3], 5) == _expected([3], 5)

# Edge handling: empty list

def test_empty_list():
    assert will_it_fly([], 0) == _expected([], 0)
    assert will_it_fly([], 10) == _expected([], 10)

# Nonâpalindromic lists should fail even if weight permits

def test_non_palindrome():
    assert will_it_fly([1, 2, 3], 100) == _expected([1, 2, 3], 100)
    assert not will_it_fly([1, 2, 3], 0)  # sum > 0, not balanced

# Cases where the sum exceeds the maximum weight

def test_sum_exceeds():
    assert not will_it_fly([5, 5, 5], 10)  # palindrome but sum 15 > 10

# Boundary condition: sum exactly equals weight

def test_sum_equals_max():
    lst = [5, 2, 5]
    w = 12  # sum 12
    assert will_it_fly(lst, w) == _expected(lst, w)

def will_it_fly(q, w):
    """Return True iff *q* is a palindrome and its elements sum to <= *w*.

    Parameters
    ----------
    q : list[int]
        The list to test.  Must be a list instance.
    w : int | float
        The maximum allowable weight.  Must be numeric.

    Returns
    -------
    bool
        True when *q* is palindromic and ``sum(q) <= w``; otherwise False.

    Raises
    ------
    TypeError
        If *q* is not a list or *w* is not a number.
    """
    if not isinstance(q, list):
        raise TypeError("q must be a list")
    if not isinstance(w, (int, float)):
        raise TypeError("w must be numeric")

    return (q == q[::-1]) and (sum(q) <= w)

def test_check():

    # Check some simple cases
    assert will_it_fly([3, 2, 3], 9) is True
    assert will_it_fly([1, 2], 5) is False
    assert will_it_fly([3], 5) is True
    assert will_it_fly([3, 2, 3], 1) is False


    # Check some edge cases that are easy to work out by hand.
    assert will_it_fly([1, 2, 3], 6) is False
    assert will_it_fly([5], 5) is True





