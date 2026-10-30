import pytest

# Helper used only in tests to recompute the expected outcome.
# This mirrors the specification logic and satisfies the "verify expected result" guideline.

def expected_is_sorted(lst: list[int]) -> bool:
    # Check for ascending order
    for i in range(len(lst) - 1):
        if lst[i] > lst[i + 1]:
            return False
    # Count duplicates
    from collections import Counter
    return all(count <= 2 for count in Counter(lst).values())


# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# Test cases
# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

def test_single_element():
    """A list of length one is always sorted and meets the duplicate rule."""
    assert is_sorted([5]) is True, "Expected True for a single-element list"


def test_empty_list():
    """An empty list should return True â treated as sorted with no duplicates."""
    assert is_sorted([]) is True, "Expected True for an empty list"


def test_already_sorted_no_duplicates():
    """Regular ascending list with unique elements should return True."""
    lst = [1, 2, 3, 4, 5]
    assert is_sorted(lst) is True


def test_unsorted_list():
    """List that is not sorted should return False."""
    lst = [1, 3, 2, 4, 5]
    assert is_sorted(lst) is False


def test_allowed_duplicates():
    """Each number appears at most twice â should return True."""
    lst = [1, 2, 2, 3, 3, 4]
    assert is_sorted(lst) is True


def test_excessive_duplicates():
    """A number appears more than twice â should return False."""
    lst = [1, 2, 2, 2, 3, 4]
    assert is_sorted(lst) is False


def test_type_validation_int_input():
    """Nonâlist input should raise TypeError (assumed implementation)."""
    with pytest.raises(TypeError):
        is_sorted(5)


def test_type_validation_string_input():
    """String input should also raise TypeError."""
    with pytest.raises(TypeError):
        is_sorted("not a list")


# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ
# Additional dataâdriven tests using the helper for expected value
# ââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââââ

def test_helper_vs_actual():
    """Crossâcheck that the helper logic matches the functionâs output for random cases."""
    import random
    for _ in range(20):
        size = random.randint(0, 10)
        lst = [random.randint(0, 5) for _ in range(size)]
        # The helper may not ensure the list is sorted; we sort it if needed.
        # However, to mimic realistic inputs, we keep the random list.
        expected = expected_is_sorted(lst)
        result = is_sorted(lst)
        assert result == expected, f"Mismatch for {lst}: expected {expected}, got {result}"

