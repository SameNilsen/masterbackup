def test_sum_squares_empty():
    """Verify that an empty list returns a sum of 0."""
    assert sum_squares([]) == 0


def test_sum_squares_basic():
    """Test a small list that triggers a square and a normal element."""
    assert sum_squares([1, 2, 3]) == 6


def test_sum_squares_negative():
    """Validate that negative values are correctly squared or cubed.
    Example from specification: [-1, -5, 2, -1, -5] should sum to -126.
    """
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_cube_only():
    """Index 4 is a multiple of 4 but not of 3, so its element must be cubed."""
    lst = [1, 0, 0, 0, 5]  # index 0 => square, index 4 => cube, others unchanged
    expected = 1 ** 2 + 5 ** 3  # 1 + 125 = 126
    assert sum_squares(lst) == expected


def test_sum_squares_overlaps_and_multiples():
    """Test indices that are multiples of 3, multiples of 4, and multiples of both (12)
    using a list of values 1 to 13. Preâcomputed expected sum is 1231.
    """
    lst = list(range(1, 14))  # indexes 0..12 with values 1..13
    # Compute expected value manually for clarity:
    expected = (
        1 ** 2 +          # index 0
        2 +                # index 1
        3 +                # index 2
        4 ** 2 +           # index 3 (multiple of 3)
        5 ** 3 +           # index 4 (multiple of 4, not 3)
        6 +                # index 5
        7 ** 2 +           # index 6
        8 +                # index 7
        9 ** 3 +           # index 8 (multiple of 4)
        10 ** 2 +          # index 9
        11 +               # index 10
        12 +               # index 11 (neither 3 nor 4)
        13 ** 2            # index 12 (multiple of 3 and 4, precedence: square)
    )
    assert sum_squares(lst) == expected

def sum_squares(lst):
    """Return the sum of a list with elements transformed by index.

    * indices divisible by 3: value squared
    * indices divisible by 4 (but not by 3): value cubed
    * all other indices: value unchanged
    """
    total = 0
    for idx, value in enumerate(lst):
        if idx % 3 == 0:
            transformed = value ** 2
        elif idx % 4 == 0:
            transformed = value ** 3
        else:
            transformed = value
        total += transformed
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

