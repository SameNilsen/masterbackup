def expected_bad_index(arr):
    """Return the largest index of an element that is strictly less than its predecessor."""
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1


def test_no_inversion_ascending():
    arr = [1, 2, 3, 4, 5]
    assert can_arrange(arr) == expected_bad_index(arr) == -1


def test_single_element():
    arr = [42]
    assert can_arrange(arr) == expected_bad_index(arr) == -1


def test_descending_order():
    arr = [9, 8, 7, 6]
    assert can_arrange(arr) == expected_bad_index(arr) == 3


def test_first_inversion_only():
    arr = [4, 3, 5, 6]
    assert can_arrange(arr) == expected_bad_index(arr) == 1


def test_multiple_inversions():
    arr = [1, 5, 3, 4, 2, 6]
    assert can_arrange(arr) == expected_bad_index(arr) == 4


def test_empty_array():
    arr = []
    assert can_arrange(arr) == expected_bad_index(arr) == -1


def test_inversion_at_end():
    arr = [1, 2, 3, 100, 4, 5]
    assert can_arrange(arr) == expected_bad_index(arr) == 4

"""
def can_arrange(arr):
    """Return the largest index i such that arr[i] < arr[i-1].

    Parameters:
        arr (list): List of unique comparable elements.

    Returns:
        int: The greatest index where a descent occurs, or -1 if the list is
        strictly ascending (or empty/singleâelement).
    """
    # Iterate from the end toward the start to find the latest inversion.
    for i in range(len(arr) - 1, 0, -1):
        if arr[i] < arr[i - 1]:
            return i
    return -1
"""


def test_check():

    # Check some simple cases
    assert can_arrange([1,2,4,3,5])==3
    assert can_arrange([1,2,4,5])==-1
    assert can_arrange([1,4,2,5,6,7,8,9,10])==2
    assert can_arrange([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert can_arrange([])==-1

