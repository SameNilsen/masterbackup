def test_empty_list():
    assert sum_squares([]) == 0


def test_small_example():
    assert sum_squares([1, 2, 3]) == 6


def test_negative_example():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_mixed_indices():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    assert sum_squares(lst) == 210


def test_overlap_multiple_of_12():
    lst = [3] * 13  # indices 0,3,6,9,12 are multiples of 3; 4 and 8 are multiples of 4 but not 3
    assert sum_squares(lst) == 117


def test_negative_cube():
    lst = [-2, -3, -4, -5]
    # index 3 cubes -5 -> -125
    assert sum_squares(lst) == -128


def test_single_element_square():
    # index 0 is a multiple of both 3 and 4, so it should be squared
    assert sum_squares([7]) == 49


def sum_squares(lst):
    """Return the sum of the list after squaring elements at
    indices that are multiples of 3 and cubing elements at
    indices that are multiples of 4 but not multiples of 3.

    Parameters
    ----------
    lst : list[int]
        List of integers to process.

    Returns
    -------
    int
        Sum of the processed elements.
    """
    total = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:
            val = val ** 2
        elif idx % 4 == 0:  # idx % 3 != 0 already guaranteed by elif
            val = val ** 3
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

