import pytest

# Test cases for the sum_squares function

def test_sum_squares_basic():
    """Basic examples from the documentation."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

@pytest.mark.parametrize(
    "lst, expected",
    [
        # Only indices that are multiples of 3 are squared
        ([10], 10 ** 2),  # index 0
        ([10, 10], 10 + 10),  # no transformations
        ([10, 10, 10], 10 ** 2 + 10 + 10),  # index 0 squared
        ([10, 10, 10, 10], 10 ** 2 + 10 + 10 + 10),  # index 3 squared
        ([10, 10, 10, 10, 10], 10 ** 2 + 10 + 10 + 10 + 10 ** 3),  # index 3 cubed
        ([2] * 13, 48),  # comprehensive test that checks overlapping indices
    ],
)
def test_sum_squares_various(lst, expected):
    assert sum_squares(lst) == expected

def test_overlap_precedence():
    """Indices divisible by both 3 and 4 should be squared, not cubed."""
    # index 12 is divisible by both 3 and 4
    data = [3] * 13  # all values are 3
    result = sum_squares(data)
    # calculate manually: indices 0,3,6,9,12 are squared => 3^2 = 9 each
    squared_indices = 5
    expected = squared_indices * (3 ** 2) + (
        (13 - squared_indices) * 3  # remaining indices unchanged
    )
    assert result == expected

def test_negative_handling():
    """Squares of negative numbers become positive; cubes retain sign."""
    # indices: 0 -> square, 4 -> cube, 8 -> cube
    data = [-2, -3, -4, -5, -6, -7, -8, -9, -10]
    result = sum_squares(data)
    # manual calculation
    expected = (
        (-2) ** 2        # index 0
        + -3              # index 1
        + -4              # index 2
        + -5              # index 3
        + (-6) ** 3      # index 4
        + -7              # index 5
        + -8              # index 6
        + -9              # index 7
        + (-10) ** 3     # index 8
    )
    assert result == expected
def sum_squares(lst):
    """Return the sum of the list after transforming elements.

    For each element at index i:
    - If i % 3 == 0: square the element.
    - Else if i % 4 == 0: cube the element.
    - Otherwise keep the element unchanged.

    The function handles empty lists and negative values correctly.
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