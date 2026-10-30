import sys


def test_sum_squares_empty():
    """Sum of an empty list should be zero."""
    assert sum_squares([]) == 0


def test_sum_squares_index_zero_squared():
    """Index 0 is a multiple of 3, so the element should be squared."""
    lst = [-2]
    # (-2)^2 = 4
    assert sum_squares(lst) == 4


def test_sum_squares_index_three_cubed():
    """Index 3 is a multiple of 4 (but not 3), the element should be cubed."""
    lst = [0, 0, 0, 2]
    # 2^3 = 8
    assert sum_squares(lst) == 8


def test_sum_squares_index_twelve_squared_over_cubed():
    """Index 12 is a multiple of both 3 and 4; squaring takes precedence."""
    lst = [0] * 13
    lst[12] = 5
    # 5^2 = 25 (not 5^3)
    assert sum_squares(lst) == 25


def test_sum_squares_mixed_case():
    """Tests both squaring and cubing in a single small list."""
    lst = [1, 2, 3, 4]
    # index 0: 1^2 = 1
    # index 1: 2 unchanged
    # index 2: 3 unchanged
    # index 3: 4^3 = 64
    expected = 1 + 2 + 3 + 64
    assert sum_squares(lst) == expected


def test_sum_squares_large_numbers():
    """Ensure large integers are handled correctly."""
    base = 10**6
    lst = [base, base + 1, base + 2, base + 3]
    # index 0: base^2
    # index 1: unchanged
    # index 2: unchanged
    # index 3: (base+3)^3
    expected = base**2 + (base + 1) + (base + 2) + (base + 3)**3
    assert sum_squares(lst) == expected


