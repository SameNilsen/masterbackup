import pytest

@pytest.mark.parametrize(
    "arr,expected",
    [
        ([], -1),
        ([1], -1),
        ([1,2,3], -1),
        ([3,2,1], 2),
        ([1,3,2,4,6,5], 5),
        ([1,2,3,5,4,6], 4),
        ([-1,-2,-3,-4], 3),
        ([-5,-3,-1,0], -1),
        ([10,5,15,20], 1),
        ([1,2,3,0], 3),
        ([1,0,2,0,4,2], 5),
    ]
)

def test_can_arrange_expected(arr, expected):
    assert can_arrange(arr) == expected

def test_can_arrange_type_and_return():
    result = can_arrange([5,4,3])
    assert isinstance(result, int)

def test_can_arrange_only_increasing():
    assert can_arrange([1, 104, 200, 500]) == -1

def test_can_arrange_at_start():
    assert can_arrange([20,10,15]) == 1

def test_can_arrange_negative_numbers():
    assert can_arrange([-10,-5,-15]) == 2

def can_arrange(arr):
    """
    Return the largest index of an element that is less than its preceding element.
    If no such index exists, return -1. All values are unique.
    """
    result = -1
    for i in range(1, len(arr)):
        if arr[i] < arr[i - 1]:
            result = i
    return result

def test_check():

    # Check some simple cases
    assert can_arrange([1,2,4,3,5])==3
    assert can_arrange([1,2,4,5])==-1
    assert can_arrange([1,4,2,5,6,7,8,9,10])==2
    assert can_arrange([4,8,5,7,3])==4

    # Check some edge cases that are easy to work out by hand.
    assert can_arrange([])==-1

