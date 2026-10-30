def test_balanced_and_sum_le_true():
    assert will_it_fly([3, 2, 3], 9) is True

def test_balanced_and_sum_equals_w_to_true():
    assert will_it_fly([3, 2, 3], 8) is True

def test_balanced_and_sum_greater_w_to_false():
    assert will_it_fly([3, 2, 3], 7) is False

def test_unbalanced_and_sum_le_w_to_false():
    assert will_it_fly([1, 2], 5) is False

def test_single_element_and_sum_le_w_true():
    assert will_it_fly([3], 5) is True

def test_empty_list_balanced_and_sum_le_w_true():
    assert will_it_fly([], 0) is True

def test_unbalanced_complex_list_false():
    assert will_it_fly([1, 2, 3, 2, 1, 4, 1, 2, 3], 100) is False

def test_zero_sum_and_balanced_list_true():
    assert will_it_fly([0, 0], 0) is True

def test_negative_max_weight_false():
    assert will_it_fly([1], -1) is False

def will_it_fly(q, w):
    """Return True if q is a palindrome and its sum is <= w.

    Parameters
    ----------
    q : list[int]
        List of numerical weights.
    w : int | float
        Maximum allowable weight.
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





