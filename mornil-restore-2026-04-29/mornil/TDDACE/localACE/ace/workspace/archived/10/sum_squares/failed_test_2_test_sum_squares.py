def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_simple():
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_negative_example():
    # Example provided in the docstring
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_index_logic():
    # Index 0 and 3 are multiple of 3 -> square
    # Index 4 is multiple of 4 but not 3 -> cube
    # For a list of length 4, only the square rule applies
    assert sum_squares([1, 2, 3, 4]) == 22  # 1^2 + 2 + 3 + 4^2


def test_sum_squares_cubic_precedence():
    # Index 4 is a clear multiple of 4 (not 3) and should be cubed
    assert sum_squares([1, 2, 3, 4, 5]) == 147  # 1^2 + 2 + 3 + 4^2 + 5^3


def test_sum_squares_multiple12():
    # Index 12 satisfies both conditions; squaring should take precedence
    lst = [1] * 13
    assert sum_squares(lst) == 13  # every element remains 1


def test_sum_squares_large():
    # A longer list that tests many index categories
    lst = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
    # Expected sum calculated manually:
    # 0:10^2=100, 1:20, 2:30, 3:40^2=1600, 4:50^3=125000,
    # 5:60, 6:70^2=4900, 7:80^2=6400, 8:90^3=729000, 9:100^2=10000
    expected = 877110
    assert sum_squares(lst) == expected


