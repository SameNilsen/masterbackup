def test_sum_squares_examples():
    assert sum_squares([]) == 0
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126

def test_sum_squares_index_0_is_squared():
    # Index 0 should be squared, even though it is also a multiple of 4
    assert sum_squares([5, 0, 0]) == 25

def test_sum_squares_overlapping_multiples():
    # Index 12 is a multiple of both 3 and 4 â should be squared
    lst = list(range(13))          # indices 0..12
    # Replace index 12 with 2 to test the squaring effect
    lst[12] = 2
    expected = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            expected += v ** 2
        elif i % 4 == 0:
            expected += v ** 3
        else:
            expected += v
    assert sum_squares(lst) == expected

def test_sum_squares_negative_and_zero_values():
    lst = [-2, -3, -4, -5]
    # idx0: -2 -> 4
    # idx1: -3 unchanged
    # idx2: -4 unchanged
    # idx3: -5 -> 25
    # idx4: -5? actually list length 4 so index 0-3 only
    expected = 4 + (-3) + (-4) + 25
    assert sum_squares(lst) == expected

def test_sum_squares_large_input_and_cubing():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
    # idx0: 1->1
    # idx1: 2
    # idx2: 3
    # idx3: 4->16
    # idx4: 5->125
    # idx5: 6
    # idx6: 7->49
    # idx7: 8
    # idx8: 9->81
    # idx9: 10->100
    # idx10: 11
    # idx11: 12->144
    expected = 1 + 2 + 3 + 16 + 125 + 6 + 49 + 8 + 81 + 100 + 11 + 144
    assert sum_squares(lst) == expected

def test_sum_squares_does_not_modify_input():
    original = [1, 2, 3, 4]
    original_copy = original.copy()
    sum_squares(original)
    assert original == original_copy
def sum_squares(lst):
    """Return the sum of the list after transforming elements based on index:

    * if the index is a multiple of 3, the element is squared;
    * else if the index is a multiple of 4 (and not a multiple of 3), the element is cubed;
    * otherwise the element is left unchanged.

    The input list is not modified.
    """
    total = 0
    for i, v in enumerate(lst):
        if i % 3 == 0:
            transformed = v ** 2
        elif i % 4 == 0:
            transformed = v ** 3
        else:
            transformed = v
        total += transformed
    return totaldef check(candidate):

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
    
    
    # Don't remove this line: