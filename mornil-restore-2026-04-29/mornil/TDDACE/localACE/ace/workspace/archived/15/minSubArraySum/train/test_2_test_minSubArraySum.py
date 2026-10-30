def test_min_subarray_sum():
    """Test the minSubArraySum function against a variety of edge cases."""
    test_cases = [
        ([2, 3, 4, 1, 2, 4], 1),             # all positive
        ([-1, -2, -3], -6),                  # all negative
        ([1, -3, 2, -5, 4, -1], -6),          # mixed signs
        ([0, 0, 0], 0),                      # zeros only
        ([5, -10, 3, -4, 2], -11),           # mixed signs, tricky min
        ([7], 7),                            # single positive
        ([-5], -5),                          # single negative
        ([1000000, -2000000, 1], -2000000),  # large numbers
    ]
    for nums, expected in test_cases:
        result = minSubArraySum(nums)
        assert result == expected, f"Failed on {nums}: expected {expected}, got {result}"
        assert isinstance(result, int), f"Return value is not int for {nums}"

def minSubArraySum(nums: list[int]) -> int:
    """
    Return the minimum possible sum of any non-empty contiguous sub-array of `nums`.
    Raises ValueError if the input list is empty.
    """
    if not nums:
        raise ValueError("nums must contain at least one element")
    min_ending_here = min_so_far = nums[0]
    for num in nums[1:]:
        min_ending_here = min(num, min_ending_here + num)
        if min_ending_here < min_so_far:
            min_so_far = min_ending_here
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

