def test_can_arrange_decreasing():
    assert can_arrange([5,4,3,2,1]) == 4

def test_can_arrange_increasing():
    assert can_arrange([1,2,3,4,5]) == -1

def test_can_arrange_single_element():
    assert can_arrange([10]) == -1

def test_can_arrange_empty():
    assert can_arrange([]) == -1

def test_can_arrange_multiple_decreases():
    assert can_arrange([1,3,5,4,6,2]) == 5

def test_can_arrange_first_pair_decreasing():
    assert can_arrange([2,1,3,4]) == 1

def test_can_arrange_negative_numbers():
    assert can_arrange([-5,-4,-6]) == 2

def test_can_arrange_recent_decrease():
    assert can_arrange([1,2,3,0]) == 3

def test_can_arrange_all_negative_increasing():
    assert can_arrange([-3,-2,-1]) == -1

def test_can_arrange_diverse_pattern():
    assert can_arrange([10,9,8,6,7,5]) == 5

def test_can_arrange_single_decrease_later():
    assert can_arrange([1,5,3,4]) == 2

def can_arrange(arr):
    """Return the largest index where the element is less than its predecessor.

    Parameters
    ----------
    arr : list
        List of distinct numbers.

    Returns
    -------
    int
        The largest index i with arr[i] < arr[i-1], or -1 if no such index exists.
    """
    last_index = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i-1]:
            last_index = i
    return last_index

def test_check():

    # Check some simple cases
    assert can_arrange([1,2,4,3,5])==3
    assert can_arrange([1,2,4,5])==-1
    assert can_arrange([1,4,2,5,6,7,8,9,10])==2
    assert can_arrange([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert can_arrange([])==-1

