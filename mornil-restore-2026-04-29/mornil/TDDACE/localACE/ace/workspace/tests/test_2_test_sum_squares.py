import pytest

# 1ï¸â£  Empty list

def test_empty_list():
    assert sum_squares([]) == 0

# 2ï¸â£  Given examples from the specification

def test_given_examples():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

# 3ï¸â£  Mixed transformation: square at index 0 and 3, cube at index 4

def test_square_and_cube_and_unmodified():
    # indices: 0->square, 3->square, 4->cube
    assert sum_squares([1, 2, 3, 4]) == 22

# 4ï¸â£  Overlap of both conditions â index 12 is a multiple of 3 and 4

def test_overlapping_index_twelve():
    lst = list(range(13))  # 0 â¦ 12
    # Compute expected sum manually (see reasoning calculations â 882)
    expected = 882
    assert sum_squares(lst) == expected

# 5ï¸â£  Negative numbers and a large integer to check sign handling and magnitude

def test_negative_and_large_numbers():
    assert sum_squares([-2, -3, -4]) == -3
    # index 0 squares 1_000_000 -> 10^12, index 1 unchanged
    assert sum_squares([1_000_000, 5]) == 1_000_000 ** 2 + 5

# 6ï¸â£  Specific indices to guard against offâbyâone errors

def test_index_specific_cases():
    # index 0 â square
    assert sum_squares([2]) == 4
    # index 3 â square (value 2 at pos 3 become 4)
    assert sum_squares([1, 1, 1, 2]) == 7
    # index 4 â cube
    assert sum_squares([1, 1, 1, 1, 2]) == 12
    # index 8 â cube (value 2 at pos 8 become 8)
    assert sum_squares([1] * 8 + [2]) == 16
    # index 12 â both conditions; priority to square
    assert sum_squares([1] * 12 + [2]) == 16

# 7ï¸â£  Comprehensive check against a naive handâcalculation (extra safety)

def test_manual_computation_consistency():
    lst = [1, 2, 3, 4, 5, 6, 7, 8]
    manual = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            manual += v ** 2
        elif i % 4 == 0:
            manual += v ** 3
        else:
            manual += v
    assert sum_squares(lst) == manual

def sum_squares(lst):
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

