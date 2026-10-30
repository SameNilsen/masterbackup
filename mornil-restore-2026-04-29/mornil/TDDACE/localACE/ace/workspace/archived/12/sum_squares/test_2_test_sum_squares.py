"""
# Tests for the sum_squares function

def test_sum_squares_empty():
    """An empty list should return 0."""
    assert sum_squares([]) == 0


def test_sum_squares_index_zero_is_square():
    """Index 0 (multiple of both 3 and 4) must be squared."""
    assert sum_squares([3]) == 9  # 3 squared


def test_sum_squares_multiple_of_3_non_4():
    """Index 3 should be squared, other indices unchanged."""
    values = [0, 0, 0, 2]  # 0-indexed: 0,1,2,3
    expected = 0**2 + 0 + 0 + 2**2  # 0 + 4 = 4
    assert sum_squares(values) == expected


def test_sum_squares_multiple_of_4_non_3():
    """Index 4 should be cubed, other indices unchanged."""
    values = [1, 1, 1, 1, 3]  # 0,1,2,3,4
    expected = 1**2 + 1 + 1 + 1 + 3**3  # 1 + 1 + 1 + 1 + 27 = 31
    assert sum_squares(values) == expected


def test_sum_squares_multiple_of_12_only_square():
    """Index 12 is a multiple of both 3 and 4; only squaring should apply."""
    values = [2] + [0]*11 + [4]  # indices 0..12
    expected = 2**2 + 4**2  # 4 + 16 = 20
    assert sum_squares(values) == expected


def test_sum_squares_given_example():
    """Example from the docstring: should produce -126."""
    lst = [-1, -5, 2, -1, -5]
    assert sum_squares(lst) == -126


def test_sum_squares_zero_values():
    """Zero values should remain zero after squaring or cubing."""
    lst = [0, 0, 0, 0, 0]
    assert sum_squares(lst) == 0
"""


def sum_squares(lst):
    """
    This function will take a list of integers. For all entries in the list, the function shall square the integer entry if its index is a 
    multiple of 3 and will cube the integer entry if its index is a multiple of 4 and not a multiple of 3. The function will not 
    change the entries in the list whose indexes are not a multiple of 3 or 4. The function shall then return the sum of all entries. 
    
    Examples:
    For lst = [1,2,3] the output should be 6
    For lst = []  the output should be 0
    For lst = [-1,-5,2,-1,-5]  the output should be -126
    """
    total = 0
    for idx, val in enumerate(lst):
        if idx % 3 == 0:
            transformed = val ** 2
        elif idx % 4 == 0:
            transformed = val ** 3
        else:
            transformed = val
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

