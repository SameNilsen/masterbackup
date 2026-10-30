def test_min_subarray_sum_examples():
    assert minSubArraySum([2, 3, 4, 1, 2, 4]) == 1
    assert minSubArraySum([-1, -2, -3]) == -6


def test_min_subarray_sum_all_positive():
    array = [10, 5, 9, 12, 1]
    assert minSubArraySum(array) == 1


def test_min_subarray_sum_all_negative():
    array = [-4, -5, -2, -7]
    assert minSubArraySum(array) == -18


def test_min_subarray_sum_single_element():
    assert minSubArraySum([42]) == 42
    assert minSubArraySum([-999]) == -999


def test_min_subarray_sum_zero_only():
    array = [0, 0, 0, 0]
    assert minSubArraySum(array) == 0


def test_min_subarray_sum_mixed():
    array = [5, -2, 3, -4, 2]
    assert minSubArraySum(array) == -4


def test_min_subarray_sum_complex():
    array = [-1, -2, 3, -4, -5, 1, 2]
    assert minSubArraySum(array) == -9


def test_min_subarray_sum_with_zero_inside():
    array = [0, -1, 0]
    assert minSubArraySum(array) == -1
    array2 = [1, 0, -1]
    assert minSubArraySum(array2) == -1

def minSubArraySum(nums: list[int]) -> int:
    """Return the minimum sum of any nonâempty contiguous subâarray of ``nums``.
    
    The algorithm is a variant of Kadane's algorithm that tracks the smallest
    running sum. It runs in O(n) time and O(1) space.
    
    Parameters
    ----------
    nums : list[int]
        Nonâempty list of integers.
    
    Returns
    -------
    int
        Minimum subâarray sum.
    """
    if not nums:
        raise ValueError("nums must contain at least one element")
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

