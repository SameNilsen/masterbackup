import pytest

# 1. Basic sorted scenarios
@ pytest.mark.parametrize("lst", [ [5], [1, 2, 3, 4, 5], [1, 2, 3, 4, 5, 6] ])
def test_basic_sorted(lst):
    assert is_sorted(lst) is True

# 2. Unsorted lists
@ pytest.mark.parametrize("lst", [ [1, 3, 2, 4, 5], [1, 3, 2, 4, 5, 6, 7] ])
def test_unsorted(lst):
    assert is_sorted(lst) is False

# 3. Allowed duplicate counts (maximum twice per value)
@ pytest.mark.parametrize("lst", [ [1, 2, 2, 3, 3, 4], [0, 1, 1, 2] ])
def test_allowed_duplicates(lst):
    assert is_sorted(lst) is True

# 4. Exceeding duplicate limit â should be False
@ pytest.mark.parametrize("lst", [ [1, 2, 2, 2, 3, 4], [3, 3, 3, 4] ])
def test_excessive_duplicates(lst):
    assert is_sorted(lst) is False

# 5. Empty list is considered sorted
def test_empty_list():
    assert is_sorted([]) is True


def is_sorted(lst: list[int]) -> bool:
    """Return True if *lst* is sorted in ascending order and
    each number occurs at most twice.

    Parameters
    ----------
    lst : list[int]
        Nonânegative integers.

    Returns
    -------
    bool
        ``True`` if the list is sorted and the duplicate
        constraint is satisfied; otherwise ``False``.
    """
    if not lst:
        return True

    prev = lst[0]
    dup_count = 1
    for num in lst[1:]:
        if num < prev:
            return False
        if num == prev:
            dup_count += 1
            if dup_count > 2:
                return False
        else:
            dup_count = 1
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

