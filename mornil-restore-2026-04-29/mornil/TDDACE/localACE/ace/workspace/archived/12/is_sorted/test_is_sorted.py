def test_is_sorted_single_element():
    assert is_sorted([5]) is True

def test_is_sorted_sorted_unique():
    assert is_sorted([1, 2, 3, 4, 5]) is True

def test_is_sorted_sorted_with_one_duplicate():
    # Duplicate allowed up to two occurrences
    assert is_sorted([1, 2, 2, 3, 3, 4]) is True

def test_is_sorted_multiple_duplicates_allowed():
    # Several numbers each appearing at most twice
    assert is_sorted([1, 1, 2, 2, 3, 3]) is True

def test_is_sorted_sorted_with_single_double():
    assert is_sorted([1, 2, 3, 3, 4]) is True

def test_is_sorted_unordered():
    assert is_sorted([1, 3, 2, 4, 5]) is False

def test_is_sorted_unsorted_with_duplicates():
    assert is_sorted([1, 2, 4, 3, 3]) is False

def test_is_sorted_exceeds_two_occurrences():
    assert is_sorted([1, 2, 2, 2, 3, 4]) is False

def test_is_sorted_three_occurrences_of_same():
    assert is_sorted([1, 1, 1]) is False

def test_is_sorted_empty_list():
    # The problem statement does not prescribe behaviour, but a sorted list can be empty
    assert is_sorted([]) is True

def test_is_sorted_returns_bool():
    assert isinstance(is_sorted([1, 2, 3]), bool)


def is_sorted(lst: list[int]) -> bool:
    """Return True if *lst* is sorted in nonâdecreasing order and
    no element appears more than twice.

    Parameters
    ----------
    lst:
        List of nonânegative integers (assumed by the problem statement).

    Returns
    -------
    bool
        ``True`` if the conditions are satisfied, otherwise ``False``.
    """

    counts = {}
    prev = None
    for i, num in enumerate(lst):
        # Count occurrences
        counts[num] = counts.get(num, 0) + 1
        if counts[num] > 2:
            return False
        # Check order
        if prev is not None and num < prev:
            return False
        prev = num
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

