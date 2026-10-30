def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_single_square():
    assert sum_squares([2]) == 4  # 0 is multiple of 3 â square


def test_sum_squares_example1():
    # [1, 2, 3] â 1^2 + 2 + 3 = 6
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_example3():
    # [-1, -5, 2, -1, -5]
    # 0: square (-1)^2 = 1
    # 3: square (-1)^2 = 1
    # 4: cube (-5)^3 = -125
    # Others unchanged
    expected = 1 + (-5) + 2 + 1 + (-125)
    assert sum_squares([-1, -5, 2, -1, -5]) == expected


def test_sum_squares_multiple_indices():
    lst = [2, 3, 4, 5, 6]
    # index 0: square 2^2 = 4
    # index 1: unchanged 3
    # index 2: unchanged 4
    # index 3: cube 5^3 = 125
    # index 4: cube 6^3 = 216 (4 is multiple of 4, not 3)
    expected = 4 + 3 + 4 + 125 + 216
    assert sum_squares(lst) == expected


def test_sum_squares_negative_numbers():
    lst = [-2, -3, -4]
    # index 0: square (-2)^2 = 4
    # index 1: unchanged -3
    # index 2: unchanged -4
    expected = 4 + (-3) + (-4)
    assert sum_squares(lst) == expected


def test_sum_squares_non_special_indices():
    # indices 1,2,5 are all not multiples of 3 or 4
    lst = [10, 11, 12, 13, 14, 15]
    # index 0 square 10^2 = 100
    # indices 1,2 unchanged
    # index 3 unchanged
    # index 4 unchanged
    # index 5 unchanged
    expected = 100 + 11 + 12 + 13 + 14 + 15
    assert sum_squares(lst) == expected


