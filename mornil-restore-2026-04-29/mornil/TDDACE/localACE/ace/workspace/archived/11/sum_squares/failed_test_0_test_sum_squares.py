def test_empty_list():
    assert sum_squares([]) == 0


def test_basic_example():
    assert sum_squares([1, 2, 3]) == 6


def test_negative_example():
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_mixed_indices():
    lst = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    expected = 0
    for i in range(len(lst)):
        if i % 3 == 0:
            expected += lst[i] ** 2
        elif i % 4 == 0:
            expected += lst[i] ** 3
        else:
            expected += lst[i]
    assert sum_squares(lst) == expected


def test_overlapping_multiples():
    lst = list(range(13))  # indices 0..12
    # Preâcomputed expected sum for this list according to the rules
    expected = 2202
    assert sum_squares(lst) == expected


def test_single_cube():
    lst = [0, 0, 0, 0, 5]
    # Only indexâ¯4 is a multiple ofâ¯4 but notâ¯3 â cube 5**3
    assert sum_squares(lst) == 125


def test_zero_values():
    lst = [0, 0, 0, 0, 0]
    assert sum_squares(lst) == 0


