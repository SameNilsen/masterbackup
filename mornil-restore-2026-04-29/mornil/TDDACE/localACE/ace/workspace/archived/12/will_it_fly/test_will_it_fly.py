def test_balanced_and_within_weight():
    assert will_it_fly([3, 2, 3], 9) is True

def test_unbalanced_and_within_weight():
    assert will_it_fly([1, 2], 5) is False

def test_balanced_exceeds_weight():
    assert will_it_fly([3, 2, 3], 1) is False

def test_single_element_balanced_within_weight():
    assert will_it_fly([3], 5) is True

def test_empty_list_balanced_within_weight():
    # An empty list is a palindrome and has sum 0, so the function should return True
    assert will_it_fly([], 0) is True

def test_negative_elements_balanced_and_within_weight():
    # Negative numbers still count toward the sum
    assert will_it_fly([-1, -2, -1], 5) is True

def test_sum_equals_max_weight():
    assert will_it_fly([5], 5) is True

def will_it_fly(q: list[int], w: int) -> bool:
    """Return True if the list q is a palindrome and its sum is less than or equal to w."""
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

