def test_basic_example():\n    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]\n\n\n# Empty list should return an empty list\n\ndef test_empty():\n    assert order_by_points([]) == []\n\n\n# All numbers have identical digit sums â test descending index tieâbreaker\n\ndef test_same_sum_descending_index():\n    nums = [111, 12, 3, 30]  # all have sum 3\n    # Order should be reversed according to original indices: 30, 3, 12, 111\n    assert order_by_points(nums) == [30, 3, 12, 111]\n\n\n# Duplicate values with identical sums â verify index ordering\n\ndef test_duplicates():\n    # Original indices: 10(0), 1(1), 10(2)\n    assert order_by_points([10, 1, 10]) == [10, 1, 10]\n\n\n# Mixed positive and negative numbers with same digit sum\n\ndef test_mixed_sign():\n    # 9 and -90 both sum to 9 â -90 index1 > 9 index0, so -90 comes first\n    assert order_by_points([9, -90]) == [-90, 9]\n\n\n# Test with large numbers to check efficiency and correctness\n\ndef test_large_numbers():\n    nums = [12345, -54321, 11111]  # sums: 15, 15, 5\n    # Order: 11111 (sum 5), then -54321 (sum 15, index 1), then 12345 (index 0)\n    assert order_by_points(nums) == [11111, -54321, 12345]\n\n\n# Single element list â should return the element itself\n\ndef test_single_element():\n    assert order_by_points([42]) == [42]\n\n\n# All negatives â ensuring index tieâbreaker works\n\ndef test_all_negatives():\n    # Sums: -20:2, -11:2, -5:5\n    # Order: -11 (index1), -20 (index0), -5\n    assert order_by_points([-20, -11, -5]) == [-11, -20, -5]\n

def order_by_points(nums):
    """
    Sort the list of integers in ascending order according to the sum of their digits.
    If multiple elements have the same digit sum, order them by descending original index.
    """
    if not nums:
        return []

    def digit_sum(x: int) -> int:
        return sum(int(d) for d in str(abs(x)))

    # Create a list of indices for tie-breaking
    indexed = list(enumerate(nums))  # (index, value)
    # Sort based on digit sum and descending index
    sorted_indexed = sorted(indexed, key=lambda ix: (digit_sum(ix[1]), -ix[0]))
    # Extract sorted values
    return [val for _, val in sorted_indexed]


def test_check():

    # Check some simple cases
    assert order_by_points([1, 11, -1, -11, -12]) == [-1, -11, 1, -12, 11]
    assert order_by_points([1234,423,463,145,2,423,423,53,6,37,3457,3,56,0,46]) == [0, 2, 3, 6, 53, 423, 423, 423, 1234, 145, 37, 46, 56, 463, 3457]
    assert order_by_points([]) == []
    assert order_by_points([1, -11, -32, 43, 54, -98, 2, -3]) == [-3, -32, -98, -11, 1, 2, 43, 54]
    assert order_by_points([1,2,3,4,5,6,7,8,9,10,11]) == [1, 10, 2, 11, 3, 4, 5, 6, 7, 8, 9]
    assert order_by_points([0,6,6,-76,-21,23,4]) == [-76, -21, 0, 4, 23, 6, 6]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"

