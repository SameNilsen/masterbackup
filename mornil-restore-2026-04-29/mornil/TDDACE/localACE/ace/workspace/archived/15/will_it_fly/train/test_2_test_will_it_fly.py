def test_balanced_within_weight():
    assert will_it_fly([3, 2, 3], 9) is True

def test_balanced_exceeds_weight():
    assert will_it_fly([3, 2, 3], 5) is False

def test_unbalanced_within_weight():
    assert will_it_fly([1, 2], 5) is False

def test_empty_list_positive_weight():
    assert will_it_fly([], 10) is True

def test_empty_list_negative_weight():
    assert will_it_fly([], -1) is False

def test_single_element_within_weight():
    assert will_it_fly([3], 5) is True

def test_single_element_exceeds_weight():
    assert will_it_fly([3], 2) is False

def test_mixed_sign_balanced_within_weight():
    assert will_it_fly([2, -1, 2], 100) is True

def test_balanced_zero_weight():
    assert will_it_fly([0, 0, 0], 0) is True

def test_balanced_exceeds_zero_weight():
    assert will_it_fly([1, 1, 1], 0) is False

def will_it_fly(q, w):
    """Return True if `q` is a palindrome and its sum is <= `w`."""
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

