def test_sum_squares_basic():
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_empty():
    assert sum_squares([]) == 0


def test_sum_squares_negative():
    # indices: 0->square, 1->unchanged, 2->unchanged
    assert sum_squares([-2, -3, -4]) == ( (-2) ** 2 + (-3) + (-4) )


def test_sum_squares_overlapping_indices():
    # Create a list where some indices satisfy both conditions (multiple of 12)
    lst = [2] * 13  # indices 0..12
    expected = sum(
        2 ** 2 if i % 3 == 0 else
        (2 ** 3 if i % 4 == 0 and i % 3 != 0 else 2)
        for i in range(len(lst))
    )
    result = sum_squares(lst)
    assert result == expected
    # Ensure the original list is unchanged
    assert lst == [2] * 13


def test_sum_squares_no_modification():
    # Test that the function does not mutate the input list
    original = [5, 10]
    _ = sum_squares(original)
    assert original == [5, 10]


def test_sum_squares_return_type():
    assert isinstance(sum_squares([1, 2, 3]), int)
def sum_squares(lst):
    """Return the sum after transforming elements based on their index.

    * Square the element if its index is a multiple of 3.
    * Cube the element if its index is a multiple of 4 but not a multiple of 3.
    * Leave other elements unchanged.
    The input list is never modified.
    """
    return sum(
        val ** 2 if i % 3 == 0 else
        val ** 3 if i % 4 == 0 else
        val
        for i, val in enumerate(lst)
    )