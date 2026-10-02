def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_indices_multiple_of_three():
    # Indices 0, 3, 6 should be squared
    lst = [2, 3, 4, 5, 6, 7, 8]
    # Expected sum: 2^2 + 3 + 4 + 5^2 + 6 + 7 + 8^2
    expected = 4 + 3 + 4 + 25 + 6 + 7 + 64
    assert sum_squares(lst) == expected


def test_sum_squares_indices_multiple_of_four_not_three():
    # Only index 4 is multiple of 4 (not multiple of 3)
    lst = [0, 1, 2, 3, 4]
    # Expected: 0 + 1 + 2 + 3 + 4^3 = 0 + 1 + 2 + 3 + 64
    expected = 70
    assert sum_squares(lst) == expected


def test_sum_squares_index_multiple_of_twelve_squared():
    # Index 12 is multiple of both 3 and 4; should be squared
    lst = list(range(13))  # 0 to 12
    # Sum 0..12 = 78; replace 12 with 12^2=144 (difference +132)
    expected = 78 + 132
    assert sum_squares(lst) == expected


def test_sum_squares_immutability():
    original = [1, 2, 3, 4, 5]
    copy = original.copy()
    sum_squares(original)
    assert original == copy  # the original list should remain unchangeddef sum_squares(lst):
    """Return the sum of a transformed list.

    For each element in *lst*, if its index is a multiple of 3 the element
    is squared; if its index is a multiple of 4 and not a multiple of 3 it
    is cubed.  Elements at other indices remain unchanged.  The original list
    is not modified.
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
def check(candidate):

    # Check some simple cases
    
    assert candidate([1,2,3]) == 6
    assert candidate([1,4,9]) == 14
    assert candidate([]) == 0
    assert candidate([1,1,1,1,1,1,1,1,1]) == 9
    assert candidate([-1,-1,-1,-1,-1,-1,-1,-1,-1]) == -3
    assert candidate([0]) == 0
    assert candidate([-1,-5,2,-1,-5]) == -126
    assert candidate([-56,-99,1,0,-2]) == 3030
    assert candidate([-1,0,0,0,0,0,0,0,-1]) == 0
    assert candidate([-16, -9, -2, 36, 36, 26, -20, 25, -40, 20, -4, 12, -26, 35, 37]) == -14196
    assert candidate([-1, -3, 17, -1, -15, 13, -1, 14, -14, -12, -5, 14, -14, 6, 13, 11, 16, 16, 4, 10]) == -1448
    
    
    # Don't remove this line:def sum_squares(lst):
    """Return the sum of the list after transforming elements based on their indices.

    * Square elements whose indices are multiples of 3.
    * Cube elements whose indices are multiples of 4 but not multiples of 3.
    * Leave other elements unchanged.

    The input list is not modified.
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