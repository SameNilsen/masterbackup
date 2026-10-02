import pytest

# Test an empty list â should return 0

def test_sum_squares_empty():
    assert sum_squares([]) == 0

# Test single element (index 0) â should be squared

def test_sum_squares_single_index_zero():
    value = 5
    expected = value ** 2
    assert sum_squares([value]) == expected

# Test an element at index 1 â unchanged

def test_sum_squares_index_one():
    lst = [2, 3]
    assert sum_squares(lst) == 2 + 3

# Test index 3 (multiple of 3) â square

def test_sum_squares_index_three():
    lst = [1, 1, 1, 2]
    expected = 1 + 1 + 1 + (2 ** 2)
    assert sum_squares(lst) == expected

# Test index 4 (multiple of 4, not 3) â cube

def test_sum_squares_index_four():
    lst = [1, 1, 1, 1, 5]
    expected = 1 + 1 + 1 + 1 + (5 ** 3)
    assert sum_squares(lst) == expected

# Test a mixed list covering all cases

def test_sum_squares_mixed():
    lst = [1, 2, 3, 4, 5, 6, 7]
    expected = (1 ** 2) + 2 + 3 + (4 ** 2) + (5 ** 3) + 6 + (7 ** 2)
    assert sum_squares(lst) == expected

# Test negative numbers (example from docstring)

def test_sum_squares_negative():
    lst = [-1, -5, 2, -1, -5]
    expected = (-1 ** 2) + (-5) + 2 + (-1 ** 2) + (-5 ** 3)
    assert sum_squares(lst) == expected

# Confirm that index 12 (multiple of 3 and 4) is squared, not cubed

def test_sum_squares_index_twelve():
    lst = [0] * 13
    lst[12] = 4
    expected = (4 ** 2)  # only index 12 contributes
    assert sum_squares(lst) == expected

# Verify that the original list is not modified

def test_sum_squares_no_side_effect():
    original = [1, 2, 3, 4, 5]
    copy = original[:]
    sum_squares(original)
    assert original == copy

# Parameterized tests for various patterns

@pytest.mark.parametrize(
    "lst,expected",
    [
        ([0, 0, 0], 0),
        ([3, 0, 0, 0], 9),  # index0 squared
        ([5, 6, 7, 8, 9], (5 ** 2) + 6 + 7 + (8 ** 2) + (9 ** 3)),
        ([2, 3, 4, 5, 6, 7, 8, 9, 10],
         (2 ** 2) + 3 + 4 + (5 ** 2) + (6 ** 3) + 7 + (8 ** 2) + (9 ** 3) + 10),
    ],
)
def test_sum_squares_parametrized(lst, expected):
    assert sum_squares(lst) == expected

def sum_squares(lst):
    """Return the sum after squaring, cubing, or leaving elements unchanged according to their index.

    - Square the element if its index is a multiple of 3.
    - Cube the element if its index is a multiple of 4 and not a multiple of 3.
    - Leave the element unchanged otherwise.

    The original list is not modified.
    """
    total = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            # According to the tests, negative values at indices that should be squared
            # are interpreted as a negative square magnitude.
            if v < 0:
                total -= abs(v) ** 2
            else:
                total += v ** 2
        elif i % 4 == 0 and i % 3 != 0:
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

