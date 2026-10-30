def test_sum_squares_zero_input():
    assert sum_squares([]) == 0


def test_sum_squares_basic_example():
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_negative_numbers():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_overlapping_indices():
    lst = list(range(13))
    assert sum_squares(lst) == 882
    # Ensure the function does not mutate the original list
    assert lst == list(range(13))


def test_sum_squares_single_element():
    assert sum_squares([5]) == 25


def test_sum_squares_boundary_three():
    assert sum_squares([2, 3, 4]) == 11


def test_sum_squares_boundary_four():
    assert sum_squares([2, 3, 4, 5]) == 36


def test_sum_squares_unchanged_other_indices():
    test_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
    assert sum_squares(test_list) == 717
    assert test_list == [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


def test_sum_squares_negative_mixed():
    test_list = [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]
    assert sum_squares(test_list) == -1431
    assert test_list == [-3, -4, -5, -6, -7, -8, -9, -10, -11, -12]

def sum_squares(lst):
    """Return the sum of elements transformed per index rules.

    For each element at position i in *lst*:
    - If i is a multiple of 3, square the element.
    - Else if i is a multiple of 4 (and not a multiple of 3), cube the element.
    - Otherwise leave the element unchanged.

    The function returns the sum of the resulting list.

    Examples
    --------
    >>> sum_squares([1, 2, 3])
    6
    >>> sum_squares([])
    0
    """
    total = 0
    for idx, value in enumerate(lst):
        if idx % 3 == 0:
            transformed = value ** 2
        elif idx % 4 == 0:
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

