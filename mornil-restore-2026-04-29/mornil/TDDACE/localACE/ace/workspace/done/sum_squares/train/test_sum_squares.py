def test_sum_squares_basic():
    lst = [1, 2, 3]
    assert sum_squares(lst) == 6


def test_sum_squares_empty():
    lst = []
    assert sum_squares(lst) == 0


def test_sum_squares_negative_example():
    lst = [-1, -5, 2, -1, -5]
    assert sum_squares(lst) == -126


def test_sum_squares_multiples_of_three():
    # indices 0 and 3 and 6 are multiples of 3
    lst = [2, 3, 4, 5, 6, 7, 8]
    # 0: 2^2 = 4, 3: 5^2 = 25, 6: 8^2 = 64; others unchanged
    expected = 4 + 3 + 4 + 25 + 216 + 7 + 64  # 216 comes from index 4 cubed (4^3)
    assert sum_squares(lst) == expected


def test_sum_squares_multiples_of_four():
    # index 4 is the only multiple of 4 not a multiple of 3
    lst = [2, 3, 4, 5, 6]
    # 4: 6^3 = 216; others unchanged except index 0 (3) and index 3 (multiple of 3)
    expected = 4 + 3 + 4 + 25 + 216  # 0: 2^2=4, 3:5^2=25
    assert sum_squares(lst) == expected


def test_sum_squares_intersection_multiples():
    # index 12 is a multiple of both 3 and 4 (should be squared, not cubed)
    lst = list(range(13))  # 0 through 12
    expected = 0 + 1 + 2 + 9 + 64 + 5 + 36 + 7 + 512 + 81 + 10 + 11 + 144
    assert sum_squares(lst) == expected  # 882


def test_sum_squares_zero_and_negative_indices():
    lst = [-1, 2, 3, 4, -5]
    # 0: (-1)^2=1, 3: 4^2=16, 4: (-5)^3=-125
    expected = 1 + 2 + 3 + 16 - 125
    assert sum_squares(lst) == expected


def test_sum_squares_all_zeroes():
    lst = [0, 0, 0, 0]
    assert sum_squares(lst) == 0

def sum_squares(lst: list[int]) -> int:
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




