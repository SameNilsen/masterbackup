def test_sum_squares_empty():
    """Empty list should return 0."""
    assert sum_squares([]) == 0


def test_sum_squares_single_square():
    """Index 0 is divisible by 3 â the element is squared."""
    assert sum_squares([5]) == 25   # 5**2


def test_sum_squares_single_cube():
    """Index 4 is divisible by 4 but not by 3 â the element is cubed."""
    assert sum_squares([0, 0, 0, 0, 3]) == 27   # 3**3


def test_sum_squares_example_negative():
    """Example from the docstring with negative values."""
    assert sum_squares([-1, -5, 2, -1, -5]) == -126


def test_sum_squares_multiple_of_twelve():
    """Index 12 is a multiple of both 3 and 4; it should be squared, not cubed."""
    values = [2] * 13  # 13 elements; index 12 has value 2
    expected = 48
    assert sum_squares(values) == expected


def test_sum_squares_negative_cube():
    """Negative number at an index divisible only by 4 is cubed, preserving sign."""
    # Index 0: â1 -> squared = 1
    # Index 4: â2 -> cubed = â8
    # Other indices remain 0
    assert sum_squares([-1, 0, 0, 0, -2]) == -7

def sum_squares(lst):
    """Return the sum of list elements after squaring or cubing based on index.

    For each element in *lst*:
        - Square it if its index is a multiple of 3.
        - Cube it if its index is a multiple of 4 but not a multiple of 3.
        - Leave it unchanged otherwise.

    Parameters
    ----------
    lst : list[int]
        List of integers to process.

    Returns
    -------
    int
        Sum of the transformed elements.
    """
    total = 0
    for i, val in enumerate(lst):
        if i % 3 == 0:
            val = val ** 2
        elif i % 4 == 0 and i % 3 != 0:
            val = val ** 3
        total += val
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

