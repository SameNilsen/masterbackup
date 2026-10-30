def test_sum_squares_square_at_index_0_only():
    """Only index 0 (multiple of 3) should be squared."""
    lst = [2, 5, 7]
    # 2^2 + 5 + 7 = 4 + 5 + 7 = 16
    assert sum_squares(lst) == 16
    # The list itself should remain unchanged
    assert lst == [2, 5, 7]


def test_sum_squares_negative_and_zero_values():
    """Check behaviour on the documented negative example and an allâzero list."""
    # Example from the docstring
    example = [-1, -5, 2, -1, -5]
    # 1 + (-5) + 2 + 1 + (-125) = -126
    assert sum_squares(example) == -126

    # All zeros should sum to zero
    zeros = [0, 0, 0, 0, 0]
    assert sum_squares(zeros) == 0


def test_sum_squares_empty_list():
    """An empty list should return zero."""
    assert sum_squares([]) == 0


def test_sum_squares_cubes_at_eight_and_four():
    """Indices 4 and 8 are multiples of 4 but not 3; they should be cubed."""
    lst = [2, 3, 4, 5, 2]
    # index 0: 2^2 = 4
    # index 1: 3
    # index 2: 4
    # index 3: 5 (multiple of 3) => 5^2 = 25
    # index 4: 2 (multiple of 4) => 2^3 = 8
    expected = 4 + 3 + 4 + 25 + 8
    assert sum_squares(lst) == expected


def test_sum_squares_multiple_of_twelve_squared_only():
    """Index 12 is a multiple of both 3 and 4; it should be squared only."""
    # Build a list where only indices 0,4,8,12 have nonâzero values
    lst = [3, 0, 0, 0, 2, 0, 0, 0, 2, 0, 0, 0, 3]
    # index 0: 3^2 = 9
    # index 4: 2^3 = 8
    # index 8: 2^3 = 8
    # index 12: 3^2 = 9
    expected = 9 + 8 + 8 + 9
    assert sum_squares(lst) == expected


def test_sum_squares_edge_case_multiple_of_three_and_four():
    """Test that indices that are multiples of 3 *and* 4 are squared, not cubed."""
    # Index 12 is the only such index in this list
    lst = [1, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 2]
    # index 0: 1^2 = 1
    # index 12: 2^2 = 4
    expected = 1 + 4
    assert sum_squares(lst) == expected

def sum_squares(lst):
    """Return the sum of the list after applying the transformation rules.

    For each element at index ``i``:
        * If ``i`` is a multiple of 3, the element is squared.
        * Else if ``i`` is a multiple of 4 (and not a multiple of 3), the element is cubed.
        * Otherwise the element remains unchanged.

    The original list is not modified.
    """
    total = 0
    for i, value in enumerate(lst):
        if i % 3 == 0:
            transformed = value ** 2
        elif i % 4 == 0:
            transformed = value ** 3
        else:
            transformed = value
        total += transformed
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

