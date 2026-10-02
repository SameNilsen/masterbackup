import pytest


def test_sum_squares_examples():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_index_rules():
    lst = [2, 3, 4, 5, 6, 7, 8, 9]
    # index 0,3,6 -> squares; index 4 -> cube; others unchanged
    expected = 4 + 3 + 4 + 25 + 216 + 7 + 64 + 9  # 332
    assert sum_squares(lst) == expected


def test_sum_squares_negative_numbers():
    lst = [-2, -3, -4, -5]
    # 0 square, 1 unchanged, 2 unchanged, 3 square
    expected = 4 + (-3) + (-4) + 25  # 22
    assert sum_squares(lst) == expected


def test_sum_squares_no_mutation():
    original = [1, 4, 9, 16]
    lst_copy = original.copy()
    sum_squares(original)
    assert original == lst_copy, "The function should not modify the original list"
def sum_squares(lst):
    """Return the sum of list elements after transforming values based on index rules.

    * Square the element if index is a multiple of 3.
    * Cube the element if index is a multiple of 4 but not a multiple of 3.
    * Leave the element unchanged otherwise.
    The original list is not modified.
    """
    total = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:
            total += val ** 2
        elif idx % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total