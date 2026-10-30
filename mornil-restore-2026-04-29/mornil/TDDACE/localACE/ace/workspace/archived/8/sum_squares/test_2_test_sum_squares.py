def test_example_cases():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_index_0_is_squared():
    # Index 0 is a multiple of 3, so it must be squared
    assert sum_squares([3]) == 3 ** 2


def test_index_4_cubed_and_other_indices_unmodified():
    # Only index 4 is modified (cubed); others remain unchanged
    lst = [-2, -2, -2, -2, -2]
    expected = (-2) * 4 + (-2) ** 3  # four untouched elements + cubed element
    assert sum_squares(lst) == expected


def test_index_12_squared_not_cubed():
    # Index 12 is a multiple of both 3 and 4; it should be squared only
    lst = list(range(13))  # indices 0-12
    # Manually compute expected sum
    expected = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            expected += v ** 2
        elif i % 4 == 0:
            expected += v ** 3
        else:
            expected += v
    assert sum_squares(lst) == expected


def test_mixed_indices_long_list():
    # A longer list to exercise several branches
    lst = list(range(20))
    result = sum_squares(lst)
    # Verify by recomputing manually
    manual = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            manual += v ** 2
        elif i % 4 == 0:
            manual += v ** 3
        else:
            manual += v
    assert result == manual

def sum_squares(lst):
    """
    Takes a list of integers and returns the sum after modifying elements
    based on their indices as follows:
      - If the index is a multiple of 3, square the element.
      - Else if the index is a multiple of 4, cube the element.
      - Otherwise leave the element unchanged.

    Index 0 is considered a multiple of 3 and therefore will be squared.
    """
    total = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            total += v ** 2
        elif i % 4 == 0:
            total += v ** 3
        else:
            total += v
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

