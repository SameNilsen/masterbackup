def _brute_min_subarray_sum(nums):
    min_sum = float('inf')
    for i in range(len(nums)):
        cur_sum = 0
        for j in range(i, len(nums)):
            cur_sum += nums[j]
            if cur_sum < min_sum:
                min_sum = cur_sum
    return min_sum


def test_min_subarray_sum_example_positive():
    nums = [2, 3, 4, 1, 2, 4]
    assert minSubArraySum(nums) == 1
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_example_negative():
    nums = [-1, -2, -3]
    assert minSubArraySum(nums) == -6
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_all_positive():
    nums = [5, 6, 7, 10]
    assert minSubArraySum(nums) == 5
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_all_negative():
    nums = [-4, -3, -2, -5]
    assert minSubArraySum(nums) == sum(nums)
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_mixed_numbers():
    nums = [5, -10, 5, 2]
    assert minSubArraySum(nums) == -10
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_single_positive():
    nums = [10]
    assert minSubArraySum(nums) == 10
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_single_negative():
    nums = [-15]
    assert minSubArraySum(nums) == -15
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_with_zero():
    nums = [0, 3, -1, 2]
    assert minSubArraySum(nums) == -1
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_all_zeros():
    nums = [0, 0, 0]
    assert minSubArraySum(nums) == 0
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)


def test_min_subarray_sum_large_random():
    import random
    nums = [random.randint(-100, 100) for _ in range(50)]
    assert minSubArraySum(nums) == _brute_min_subarray_sum(nums)

def minSubArraySum(nums):
    """
    Return the minimum sum of any nonâempty subâarray of nums.

    Parameters
    ----------
    nums : list[int]
        List of integers; must be nonâempty.

    Returns
    -------
    int
        Minimum subâarray sum.

    Raises
    ------
    TypeError
        If ``nums`` is not an instance of ``list`` (or any sequence).
    ValueError
        If ``nums`` is empty.
    """
    # Input validation â see playbook bullet *saiâ00008* and *errâ00009*
    if not isinstance(nums, list):
        raise TypeError("nums must be a list of integers")
    if not nums:
        raise ValueError("nums must contain at least one element")

    # Kadane's algorithm for minimum subâarray sum
    min_ending_here = nums[0]
    min_so_far = nums[0]
    for num in nums[1:]:
        # Choose whether to start a new subâarray (num) or extend the previous one
        min_ending_here = min(num, min_ending_here + num)
        # Update global minimum
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




