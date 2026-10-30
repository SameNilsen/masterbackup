def test_balanced_and_within_weight():
    assert will_it_fly([1, 2, 1], 6) == True

def test_unbalanced():
    assert will_it_fly([1, 2, 3], 10) == False

def test_balanced_exceeds_weight():
    assert will_it_fly([3, 2, 3], 5) == False

def test_balanced_equal_weight():
    assert will_it_fly([3, 2, 3], 8) == True

def test_empty_list():
    assert will_it_fly([], 0) == True

def test_negative_numbers_balanced_within_weight():
    assert will_it_fly([-1, -2, -1], -3) == True

def test_negative_numbers_exceeds_weight():
    assert will_it_fly([-1, -2, -1], -5) == False

def test_weight_zero():
    assert will_it_fly([0, 0, 0], 0) == True

def test_large_list():
    assert will_it_fly([1, 2, 3, 2, 1], 9) == True
    assert will_it_fly([1, 2, 3, 2, 1], 8) == False

def will_it_fly(q, w):
    '''Return True if *q* is a palindromic list and its sum does not exceed *w*.

    Parameters
    ----------
    q : list[int]
        Sequence of numeric weights.
    w : int or float
        Maximum allowed total weight.

    Returns
    -------
    bool
        True when *q* is palindromic AND sum(q) <= w, otherwise False.
    '''
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

