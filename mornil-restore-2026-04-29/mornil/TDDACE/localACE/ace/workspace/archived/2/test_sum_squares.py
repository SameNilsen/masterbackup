def test_empty_list_results_zero():
    """The function should return 0 for an empty list."""
    assert sum_squares([]) == 0


def test_example_1_and_2():
    """Test the examples from the docstring.
    [1, 2, 3] -> indices 0 squared (1), others unchanged: 1 + 2 + 3 = 6
    [-1, -5, 2, -1, -5] -> index 0 square (1), index 3 square (1), index 4 cube (-125): 1 -5 +2 +1 -125 = -126
    """
    assert sum_squares([1, 2, 3]) == 6
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_negative_and_zero_indices():
    """Indexes 0, 3, 6, 12 are multiples of 3; they should be squared regardless of whether they are also multiples of 4.
    Index 4 and 8 are multiples of 4 but not 3; they should be cubed.
    """
    # Construct a list 0..12 inclusive so we hit all relevant cases.
    lst = list(range(13))
    # Manually compute expected sum: square where i%3==0, cube where i%4==0 and i%3!=0.
    expected = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            expected += val * val
        elif i % 4 == 0:
            expected += val ** 3
        else:
            expected += val
    assert sum_squares(lst) == expected
    assert expected == 882  # preâcomputed value to guarantee correctness


def test_negative_cubing_and_squaring():
    """Confirm proper handling of negative numbers for both squaring and cubing."""
    lst = [0, -2, -3, -4, -5]
    # Index 0: 0 squared = 0
    # Index 1,2: unchanged -2, -3
    # Index 3: -4 squared = 16
    # Index 4: -5 cubed = -125
    assert sum_squares(lst) == 0 + (-2) + (-3) + 16 + (-125)  # = -114


def test_mixed_values_and_large_range():
    """Use a larger list with varied numbers to test consistency across many indices."""
    import random
    rng = random.Random(0)
    lst = [rng.randint(-10, 10) for _ in range(50)]
    # Compute expected with the same rule in the test
    expected = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            expected += val * val
        elif i % 4 == 0:
            expected += val ** 3
        else:
            expected += val
    assert sum_squares(lst) == expected
def sum_squares(lst):
    """Return the sum of the list after transforming elements based on index.
    Elements whose indices are multiples of 3 are squared.
    Elements whose indices are multiples of 4 (but not multiples of 3) are cubed.
    All other elements remain unchanged.
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            total += val * val
        elif i % 4 == 0:
            total += val ** 3
        else:
            total += val
    return total