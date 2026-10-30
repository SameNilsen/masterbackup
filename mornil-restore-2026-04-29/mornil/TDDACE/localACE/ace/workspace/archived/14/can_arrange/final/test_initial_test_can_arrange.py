def test_non_decreasing():
    assert can_arrange([1, 2, 3]) == -1
    assert can_arrange([5]) == -1
    assert can_arrange([]) == -1

def test_strictly_decreasing():
    assert can_arrange([5, 4, 3, 2, 1]) == 4
    assert can_arrange([10, 5, 0]) == 2

def test_mixed_arrays():
    assert can_arrange([1, 4, 3, 2]) == 3  # both index 2 and 3 qualify, pick largest
    assert can_arrange([10, 5, 8, 2, 4]) == 3  # only index 1 and 3 qualify, pick 3

def test_negative_numbers():
    assert can_arrange([-3, -2, -5, -1]) == 2
    assert can_arrange([-10, -20, -15]) == 1

def test_single_element_or_empty():
    assert can_arrange([7]) == -1
    assert can_arrange([]) == -1

def can_arrange(arr):
    max_idx = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            max_idx = i
    return max_idx


def test_check():

    # Check some simple cases
    assert can_arrange([1,2,4,3,5])==3
    assert can_arrange([1,2,4,5])==-1
    assert can_arrange([1,4,2,5,6,7,8,9,10])==2
    assert can_arrange([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert can_arrange([])==-1

