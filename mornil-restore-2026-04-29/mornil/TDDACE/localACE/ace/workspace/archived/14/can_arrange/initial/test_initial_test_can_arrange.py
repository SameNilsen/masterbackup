def test_returns_minus_one_for_empty_and_single_element():
    assert can_arrange([]) == -1
    assert can_arrange([7]) == -1


def test_returns_minus_one_for_all_increasing():
    assert can_arrange([1, 2, 3, 4]) == -1


def test_returns_last_index_for_all_decreasing():
    assert can_arrange([5, 4, 3, 2, 1]) == 4


def test_returns_correct_index_in_mixed_patterns():
    assert can_arrange([1, 2, 4, 3, 5]) == 3
    assert can_arrange([1, 5, 2, 3, 4]) == 2
    assert can_arrange([3, 1, 4, 2, 5, 0]) == 5


def test_returns_largest_decreasing_index_when_multiple_occurrences():
    assert can_arrange([10, 20, 30, 25, 35, 40, 38]) == 6

def can_arrange(arr):
    """Return the greatest index i where arr[i] < arr[i-1].

    Parameters
    ----------
    arr : list[int]
        List of distinct integers.

    Returns
    -------
    int
        Index of the last decreasing pair or -1 if none.
    """
    n = len(arr)
    if n <= 1:
        return -1
    max_index = -1
    for i in range(1, n):
        if arr[i] < arr[i - 1]:
            max_index = i
    return max_index

def test_check():

    # Check some simple cases
    assert can_arrange([1,2,4,3,5])==3
    assert can_arrange([1,2,4,5])==-1
    assert can_arrange([1,4,2,5,6,7,8,9,10])==2
    assert can_arrange([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert can_arrange([])==-1

