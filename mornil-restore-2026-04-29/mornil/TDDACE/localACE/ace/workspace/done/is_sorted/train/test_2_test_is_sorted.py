def test_is_sorted_behavior():
    """Test the is_sorted function for sorting and duplicate constraints."""
    def expected_is_sorted(lst: list[int]) -> bool:
        """Replicates the specification: ascending order and at most two occurrences of any number."""
        # Check duplicate count
        counts = {}
        for val in lst:
            counts[val] = counts.get(val, 0) + 1
            if counts[val] > 2:
                return False
        # Check ascending order
        for i in range(1, len(lst)):
            if lst[i] < lst[i - 1]:
                return False
        return True

    test_cases = [
        ([5], True),
        ([1, 2, 3, 4, 5], True),
        ([1, 3, 2, 4, 5], False),
        ([1, 2, 3, 4, 5, 6], True),
        ([1, 2, 2, 3, 3, 4], True),
        ([1, 2, 2, 2, 3, 4], False),
        ([1, 3, 2, 4, 5, 6, 7], False),
        ([], True),
    ]

    for lst, manual_expected in test_cases:
        programmatic_expected = expected_is_sorted(lst)
        # Verify that the manually written expectation matches the helper
        assert manual_expected == programmatic_expected,
            f"Manual expectation mismatch for list {lst}"
        # Verify the function under test returns the same result
        assert is_sorted(lst) == programmatic_expected,
            f"is_sorted returned wrong result for list {lst}"

def is_sorted(lst: list[int]) -> bool:
    """Return True if *lst* is sorted in ascending order and contains
    at most two copies of any value.
    """
    # Count occurrences while checking for overruns.
    counts: dict[int, int] = {}
    for val in lst:
        counts[val] = counts.get(val, 0) + 1
        if counts[val] > 2:
            return False
    # Check nonâdecreasing order.
    for i in range(1, len(lst)):
        if lst[i] < lst[i - 1]:
            return False
    return True

def test_check():

    # Check some simple cases
    assert is_sorted([5]) == True
    assert is_sorted([1, 2, 3, 4, 5]) == True
    assert is_sorted([1, 3, 2, 4, 5]) == False
    assert is_sorted([1, 2, 3, 4, 5, 6]) == True
    assert is_sorted([1, 2, 3, 4, 5, 6, 7]) == True
    assert is_sorted([1, 3, 2, 4, 5, 6, 7]) == False, "This prints if this assert fails 1 (good for debugging!)"
    assert is_sorted([]) == True, "This prints if this assert fails 2 (good for debugging!)"
    assert is_sorted([1]) == True, "This prints if this assert fails 3 (good for debugging!)"
    assert is_sorted([3, 2, 1]) == False, "This prints if this assert fails 4 (good for debugging!)"
    
    # Check some edge cases that are easy to work out by hand.
    assert is_sorted([1, 2, 2, 2, 3, 4]) == False, "This prints if this assert fails 5 (good for debugging!)"
    assert is_sorted([1, 2, 3, 3, 3, 4]) == False, "This prints if this assert fails 6 (good for debugging!)"
    assert is_sorted([1, 2, 2, 3, 3, 4]) == True, "This prints if this assert fails 7 (good for debugging!)"
    assert is_sorted([1, 2, 3, 4]) == True, "This prints if this assert fails 8 (good for debugging!)"





