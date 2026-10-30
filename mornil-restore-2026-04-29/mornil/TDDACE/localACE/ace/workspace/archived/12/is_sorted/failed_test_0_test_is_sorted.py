def test_single_element():
    assert is_sorted([5]) is True

def test_sorted_no_duplicates():
    assert is_sorted([1, 2, 3, 4, 5]) is True

def test_sorted_with_allowed_duplicates():
    assert is_sorted([1, 2, 2, 3, 3, 4]) is True

def test_unsorted_list():
    assert is_sorted([1, 3, 2, 4, 5]) is False

def test_duplicate_more_than_two_single_value():
    assert is_sorted([1, 2, 2, 2, 3]) is False

def test_duplicate_more_than_two_multiple_values():
    assert is_sorted([1, 2, 2, 3, 3, 3, 4]) is False

def test_zero_duplicate_allowed():
    assert is_sorted([0, 0, 1, 2, 3]) is True

def test_multiple_zero_duplicates_allowed():
    assert is_sorted([1, 1, 2, 3, 4, 5, 5]) is True

def test_more_than_two_different_values():
    assert is_sorted([1, 1, 1, 2, 2, 3, 3]) is False
```

