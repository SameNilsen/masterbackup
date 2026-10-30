def test_min_subarray_sum_all_positive():
    assert minSubArraySum([1, 2, 3]) == 1

def test_min_subarray_sum_all_negative():
    assert minSubArraySum([-1, -2, -3]) == -6

def test_min_subarray_sum_mixed():
    assert minSubArraySum([2, 3, -6, 1]) == -6

def test_min_subarray_sum_single_element():
    assert minSubArraySum([10]) == 10
    assert minSubArraySum([-10]) == -10

def test_min_subarray_sum_zero_elements():
    assert minSubArraySum([0, 0, 0]) == 0

def test_min_subarray_sum_complex_case():
    assert minSubArraySum([2, -3, 1, -5, 2]) == -7

def test_min_subarray_sum_extreme_values():
    big = [10**6, -10**6, 10**6, -10**6, 10**6]
    assert minSubArraySum(big) == -10**6

def minSubArraySum(nums: list[int]) -> int:
    """Return the minimum sum of any nonâempty contiguous subâarray.

    Parameters
    ----------
    nums : list[int]
        The list of integers to examine. Must contain at least one element.

    Returns
    -------
    int
        The smallest possible sum of a contiguous subâarray.
    """
    if not nums:
        raise ValueError("Input list must contain at least one element")

    min_ending_here = nums[0]
    min_so_far = nums[0]

    for x in nums[1:]:
        min_ending_here = min(x, min_ending_here + x)
        min_so_far = min(min_so_far, min_ending_here)

    return min_so_far

# ---- optional helper for quick local checks ----
# def check(candidate):
#     assert candidate([1, 2, 3]) == 1
#     assert candidate([-1, -2, -3]) == -6
#     assert candidate([2, 3, -6, 1]) == -6
#     assert candidate([10]) == 10
#     assert candidate([-10]) == -10
#     assert candidate([0, 0, 0]) == 0
#     assert candidate([2, -3, 1, -5, 2]) == -7
#     big = [10**6, -10**6, 10**6, -10**6, 10**6]
#     assert candidate(big) == -10**6

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

