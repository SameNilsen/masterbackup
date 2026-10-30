def expected_sum_for(lst: list[int]) -> int:
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val * val
        elif i % 4 == 0:
            total += val * val * val
        else:
            total += val
    return total


def test_sum_squares_known_input():
    """Test the function against the example that mixes all rules."""
    lst = [-1, -5, 2, -1, -5]
    assert sum_squares(lst) == expected_sum_for(lst)


def test_sum_squares_empty_list():
    """The sum of an empty list should be 0."""
    assert sum_squares([]) == 0


def test_sum_squares_does_not_modify_input():
    """Ensure the function does not mutate the caller's list."""
    original = [1, 2, 3, 4, 5]
    copy = original.copy()
    sum_squares(original)
    assert original == copy


def test_sum_squares_multiple_of_four_not_three():
    """Index 4 is a multiple of 4 but not of 3; its value should be cubed."""
    lst = [0, 1, 2, 3, 4]
    assert sum_squares(lst) == expected_sum_for(lst)


def test_sum_squares_overlapping_indices():
    """Index 12 is a multiple of both 3 and 4; the square logic takes precedence."""
    lst = list(range(1, 14))  # indices 0â12
    assert sum_squares(lst) == expected_sum_for(lst)


def test_sum_squares_negative_values():
    """Verify that negative numbers are squared/cubed correctly."""
    lst = [2, 1, 0, 3, -2]
    # index 0 -> 2^2 = 4,  index 4 -> (-2)^3 = -8
    assert sum_squares(lst) == expected_sum_for(lst)

"def sum_squares(lst: list[int]) -> int:
    """Return the sum of `lst` after applying indexâbased transformations.

    For each element:
        â¢ If its index `i` is a multiple of 3, square the element.
        â¢ Else, if `i` is a multiple of 4, cube the element.
        â¢ Otherwise, keep the element unchanged.

    The input list is not modified.
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            val = val ** 2
        elif i % 4 == 0:
            val = val ** 3
        total += val
    return total
"

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




