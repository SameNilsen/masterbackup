import pytest

def test_minSubArraySum_all_positive():
    assert minSubArraySum([5, 2, 3, 1, 4]) == 1


def test_minSubArraySum_all_negative():
    assert minSubArraySum([-1, -2, -3, -4]) == -10


def test_minSubArraySum_mixed():
    assert minSubArraySum([2, -1, 2, 3, -4, 3]) == -4


def test_minSubArraySum_single_element():
    assert minSubArraySum([42]) == 42


def test_minSubArraySum_with_zero_and_negatives():
    assert minSubArraySum([5, -3, 0, -2]) == -5



def test_minSubArraySum_negative_start():
    assert minSubArraySum([-5, 1, -2, 3]) == -6


def test_minSubArraySum_all_zero():
    assert minSubArraySum([0, 0, 0]) == 0


def test_minSubArraySum_large_numbers():
    assert minSubArraySum([10**9, -10**9, 500]) == -10**9


def test_minSubArraySum_empty():
    with pytest.raises(ValueError):
        minSubArraySum([])

def minSubArraySum(nums: list[int]) -> int:
    '''Return the smallest possible sum of a contiguous subâarray in nums.

    Parameters
    ----------
    nums : list[int]
        Nonâempty sequence of integers.

    Returns
    -------
    int
        The minimal contiguous subâarray sum.

    Raises
    ------
    ValueError
        If the input list cannot be empty.
    '''
    if not nums:
        raise ValueError("Input list cannot be empty")

    cur_min = best_min = nums[0]
    for x in nums[1:]:
        cur_min = min(x, cur_min + x)
        best_min = min(best_min, cur_min)
    return best_min

def test_check():

    # Check some simple cases
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1, "This prints if this assert fails 1 (good for debugging!)"
    assert minSubArraySum([-1, -2, -3]) == -6
    assert minSubArraySum([-1, -2, -3, 2, -10]) == -14
    assert minSubArraySum([-9999999999999999]) == -9999999999999999
    assert minSubArraySum([0, 10, 20, 1000000]) == 0
    assert minSubArraySum([-1, -2, -3, 10, -5]) == -6
    assert minSubArraySum([100, -1, -2, -3, 10, -5]) == -6
    assert minSubArraySum([10, 11, 13, 8, 3, 4]) == 3
    assert minSubArraySum([100, -33, 32, -1, 0, -2]) == -33

    # Check some edge cases that are easy to work out by hand.
    assert minSubArraySum([-10]) == -10, "This prints if this assert fails 2 (also good for debugging!)"
    assert minSubArraySum([7]) == 7
    assert minSubArraySum([1, -1]) == -1

