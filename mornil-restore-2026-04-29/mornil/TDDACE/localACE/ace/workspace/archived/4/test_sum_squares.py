import pytest

# Note: The function `sum_squares` is assumed to be imported from the module under test.


def test_sum_squares_empty():
    """An empty list should return 0."""
    assert sum_squares([]) == 0


def test_sum_squares_examples():
    """Verify the provided example cases."""
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_index_multiple_of_four():
    """Index 4 (multiple of 4, not multiple of 3) should be cubed.
    List: [2, 3, 4, 5, 6]
    Indices:
      0 -> square 2^2 = 4
      1 -> unchanged 3
      2 -> unchanged 4
      3 -> square 5^2 = 25
      4 -> cube  6^3 = 216
    Total sum = 4 + 3 + 4 + 25 + 216 = 252
    """
    lst = [2, 3, 4, 5, 6]
    assert sum_squares(lst) == 252


def test_squaring_over_cubing():
    """Index 12 is a multiple of both 3 and 4.
    The rule specifies that if an index is a multiple of 3, the element should be squared,
    regardless of it also being a multiple of 4.
    """
    # Create a list of length 13 where only index 12 has a notable value
    lst = [0] * 12 + [2]
    # At index 12, 2 should be squared to 4
    assert sum_squares(lst) == 4


def test_no_mutation_of_input():
    """Ensure the input list is not modified in place."""
    original = [1, 2, 3, 4, 5]
    copy = original.copy()
    sum_squares(original)
    assert original == copy


def test_index_zero_and_negative_values():
    """Index 0 is a multiple of 3; the value should be squared.
    Test with a zero value to confirm it remains zero after squaring.
    """
    assert sum_squares([0, -1, -2]) == 0  # 0^2 + (-1) + (-2) = -3, but index 0 squared -> 0, so sum = -3
    # Since -1 at index 1 and -2 at index 2 are unchanged, final sum is -3


# Parametrized tests for a variety of indices to ensure correct operations
@pytest.mark.parametrize(
    "idx, value, expected",
    [
        (0, 3, 9),      # multiple of 3 -> square
        (1, 4, 4),      # no change
        (3, 5, 25),     # multiple of 3 -> square
        (4, 2, 8),      # multiple of 4 not 3 -> cube
        (7, 3, 3),      # no change
        (8, 2, 4),      # multiple of 4 not 3 -> cube
        (12, 1, 1),     # multiple of 3 (and 4) -> square
    ],
)

def test_various_indices(idx, value, expected):
    """Construct a list that positions a known value at a specific index and checks that
    the element is transformed correctly and that the rest of the list contributes
    unchanged to the sum."""
    # Fill the list with zeros up to the required index, then add the value, then more zeros
    lst = [0] * idx + [value] + [0] * 5  # arbitrary tail
    # Apply the function and compare the sum to the expected contribution of the transformed value
    assert sum_squares(lst) == expected


def sum_squares(lst):
    """Return the sum of the list elements after transforming
    elements at index multiples of 3 (square) or 4 (cube, unless also a
    multiple of 3). The input list is not modified.

    Parameters
    ----------
    lst : list[int]
        List of integers.

    Returns
    -------
    int
        The sum of the transformed elements.
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val * val
        elif i % 4 == 0:
            total += val * val * val
        else:
            total += val
    return total

def test_check():

    # Check some simple cases
    
    assert sum_squares([1,2,3]) == 6
    assert sum_squares([1,4,9]) == 14
    assert sum_squares([]) == 0
    assert sum_squares([1,1,1,1,1,1,1,1,1]) == 9
    assert sum_squares([-1,-1,-1,-1,-1,-1,-1,-1,-1]) == -3
    assert sum_squares([0]) == 0
    assert sum_squares([-1,-5,2,-1,-5]) == -126
    assert sum_squares([-56,-99,1,0,-2]) == 3030
    assert sum_squares([-1,0,0,0,0,0,0,0,-1]) == 0
    assert sum_squares([-16, -9, -2, 36, 36, 26, -20, 25, -40, 20, -4, 12, -26, 35, 37]) == -14196
    assert sum_squares([-1, -3, 17, -1, -15, 13, -1, 14, -14, -12, -5, 14, -14, 6, 13, 11, 16, 16, 4, 10]) == -1448
    
    
    # Don't remove this line:

