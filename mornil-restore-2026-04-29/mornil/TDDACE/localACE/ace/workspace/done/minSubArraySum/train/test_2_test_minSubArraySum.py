import pytest


def expected_min_subarray_sum(nums):
    """Return the minimum possible sum of a nonâempty contiguous subarray.
    Implements an O(nÂ²) bruteâforce algorithm.
    """
    if not nums:
        raise ValueError("input list must be nonâempty")
    n = len(nums)
    min_sum = float("inf")
    for i in range(n):
        current = 0
        for j in range(i, n):
            current += nums[j]
            if current < min_sum:
                min_sum = current
    return min_sum


def test_minSubArraySum_positive_numbers():
    nums = [1, 2, 3, 4, 5]
    assert minSubArraySum(nums) == expected_min_subarray_sum(nums)


def test_minSubArraySum_all_negative():
    nums = [-1, -2, -3, -4]
    assert minSubArraySum(nums) == expected_min_subarray_sum(nums)


def test_minSubArraySum_mixed():
    nums = [2, -5, 1, 2, 3]
    assert minSubArraySum(nums) == expected_min_subarray_sum(nums)


def test_minSubArraySum_all_zeros():
    nums = [0, 0, 0, 0]
    assert minSubArraySum(nums) == expected_min_subarray_sum(nums)


def test_minSubArraySum_single_element():
    nums = [42]
    assert minSubArraySum(nums) == expected_min_subarray_sum(nums)


def test_minSubArraySum_large_numbers():
    nums = [-100000, 200000, -150000, 50000]
    assert minSubArraySum(nums) == expected_min_subarray_sum(nums)


def test_minSubArraySum_type_validation():
    with pytest.raises(TypeError):
        minSubArraySum(None)
    with pytest.raises(TypeError):
        minSubArraySum(123)
    with pytest.raises(TypeError):
        minSubArraySum('123')


def test_minSubArraySum_empty_list_raises():
    with pytest.raises(ValueError):
        minSubArraySum([])

def minSubArraySum(nums):
    if not isinstance(nums, list):
        raise TypeError("nums must be a list")
    if len(nums) == 0:
        raise ValueError("input list must be non-empty")
    min_ending_here = min_so_far = nums[0]
    for num in nums[1:]:
        min_ending_here = min(num, min_ending_here + num)
        min_so_far = min(min_so_far, min_ending_here)
    return min_so_far

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




