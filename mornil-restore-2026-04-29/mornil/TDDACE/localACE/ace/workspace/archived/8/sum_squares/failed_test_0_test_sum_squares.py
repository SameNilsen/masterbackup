def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_single_element():
    assert sum_squares([3]) == 9


def test_sum_squares_multiple_of_3_and_4():
    # Indices 0,3,6,9,12 are multiples of 3; 4,8 are multiples of 4 but not 3.
    lst = list(range(13))  # 0 to 12
    assert sum_squares(lst) == 882


def test_sum_squares_multiple_of_4_not_3():
    lst = [2, 2, 2, 2, 2]  # index 4 -> cube 8
    expected = 2 + 2 + 2 + 2 + 8
    assert sum_squares(lst) == expected


def test_sum_squares_negatives():
    lst = [-1, -2, -3, -4]
    # index 0 square: 1, indices 1 & 2 unchanged, index 3 square: 16
    expected = 1 - 2 - 3 + 16
    assert sum_squares(lst) == expected

