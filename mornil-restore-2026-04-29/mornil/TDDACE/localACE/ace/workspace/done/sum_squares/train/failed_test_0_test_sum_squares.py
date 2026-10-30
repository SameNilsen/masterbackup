def test_sum_squares_examples():
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([]) == 0
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_complex_cases():
    # Index 0, 3, 6, ... are multiples of 3 and should be squared.
    # Index 4, 8, 10, ... are multiples of 4 (but not 3) and should be cubed.
    # Index 12 is a multiple of both; square takes precedence.
    assert sum_squares([2, 3, 4, 5, 6, 7]) == 259
    # List of 13 consecutive integers 0..12
    lst = list(range(13))
    assert sum_squares(lst) == 1872


def test_sum_squares_edge_and_type():
    # Single element at index 0 (multiple of both 3 and 4) should be squared
    assert sum_squares([2]) == 4
    # Verify return type is int
    assert isinstance(sum_squares([1, 2, 3]), int)


