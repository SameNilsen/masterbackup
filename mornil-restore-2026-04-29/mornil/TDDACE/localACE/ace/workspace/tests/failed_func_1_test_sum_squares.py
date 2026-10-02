def test_basic_examples():
    # The provided examples from the docstring
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_alternating_conditions():
    # Mixed indices: squares at 0, 3, 6; cubes at 4, 8; rest unchanged
    lst1 = [1, 2, 3, 4, 5, 6]
    # index: 0 square -> 1^2 = 1
    # index: 1 unchanged -> 2
    # index: 2 unchanged -> 3
    # index: 3 square -> 4^2 = 16
    # index: 4 cube -> 5^3 = 125
    # index: 5 unchanged -> 6
    expected1 = 1 + 2 + 3 + 16 + 125 + 6
    assert sum_squares(lst1) == expected1

    lst2 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    # compute expected directly for clarity
    expected2 = 0
    for i, v in enumerate(lst2):
        if i % 3 == 0:
            expected2 += v ** 2
        elif i % 4 == 0:
            expected2 += v ** 3
        else:
            expected2 += v
    assert sum_squares(lst2) == expected2


def test_multiple_of_both():
    # Indices that are multiples of both 3 and 4 (e.g., 0, 12) should be squared, not cubed.
    lst = list(range(13))  # indices 0..12
    expected = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            expected += v ** 2
        elif i % 4 == 0:
            expected += v ** 3
        else:
            expected += v
    assert sum_squares(lst) == expected


def test_edge_cases_and_immutability():
    # Negative numbers: squaring should turn negative to positive, cubing keeps sign
    lst_neg = [-2, -3, -4, -5]
    # idx 0 square: (-2)^2=4
    # idx 1 unchanged: -3
    # idx 2 unchanged: -4
    # idx 3 cube: (-5)^3=-125
    expected_neg = 4 + (-3) + (-4) + (-125)
    assert sum_squares(lst_neg) == expected_neg

    # Zero remains zero after any operation
    lst_zero = [0, 1, 2, 3]
    # idx 0 square: 0
    # idx 3 square: 3^2=9
    expected_zero = 0 + 1 + 2 + 9
    assert sum_squares(lst_zero) == expected_zero

    # Ensure the original list is not modified
    original = [2, 4, 6, 8, 10]
    original_copy = original.copy()
    sum_squares(original)
    assert original == original_copy

def sum_squares(lst):
    """Return the sum of transformed elements.

    Elements at indices that are multiples of 3 are squared.
    Elements at indices that are multiples of 4 (but not of 3) are cubed.
    All other elements contribute their original value.
    The original list is not modified.
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

def sum_squares(lst):
    """Return the sum of the list after altering elements based on index.

    For each element at index ``i`` in ``lst`` (0âbased):
        * if ``i % 3 == 0``: square the element (``x**2``)
        * elif ``i % 4 == 0``: cube the element (``x**3``)
        * otherwise: leave it unchanged.

    The original list is not modified.  The result is an integer.
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val ** 2
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total

