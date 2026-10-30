def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_simple_case():
    # indices: 0 (sq 1^2=1), 1 (unchanged 2), 2 (unchanged 3)
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_negative_values():
    # indices: 0 (sq -1^2=1), 1 (-5), 2 (2), 3 (sq -1^2=1), 4 (cube -5^3=-125)
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_multiple_of_four_not_three():
    # indices: 0 (sq 0^2=0), 1 (1), 2 (2), 3 (sq 3^2=9), 4 (cube 4^3=64)
    assert sum_squares([0, 1, 2, 3, 4]) == 76


def test_sum_squares_overlap_multiple_of_12():
    # list of 13 numbers from 0 to 12
    # correctly apply "square" rule on index 12 which is multiple of both 3 and 4
    values = list(range(13))
    expected_sum = 882  # preâcomputed manually
    assert sum_squares(values) == expected_sum


def sum_squares(lst):
    """
    Sum of elements of lst after transforming each element based on its index:
    * index % 3 == 0 â square the value
    * else if index % 4 == 0 (and not a multiple of 3) â cube the value
    * otherwise keep the original value
    """
    total = 0
    for idx, value in enumerate(lst):
        if idx % 3 == 0:
            total += value ** 2
        elif idx % 4 == 0:
            total += value ** 3
        else:
            total += value
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

