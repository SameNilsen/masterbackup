import pytest

# Parameterized examples to validate given cases
@pytest.mark.parametrize("grid, capacity, expected", [
    ([ [0,0,1,0], [0,1,0,0], [1,1,1,1] ], 1, 6),
    ([ [0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1] ], 2, 5),
    ([ [0,0,0], [0,0,0] ], 5, 0),
])
def test_examples(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected

# Test when all wells are empty

def test_zero_waters():
    grid = [[0,0,0], [0,0,0], [0,0,0]]
    assert max_fill(grid, 3) == 0

# Test when a well has less units than the bucket capacity

def test_less_than_capacity():
    grid = [[1,0,0], [0,0,0]]
    # 1 unit total in the first well, capacity 5 => needs one bucket
    assert max_fill(grid, 5) == 1

# Test when total units are divisible by the capacity

def test_capacity_divides_evenly():
    grid = [[1,1,1,1,1,1,1,1]]  # 8 units
    assert max_fill(grid, 2) == 4

# Stress test on a larger grid

def test_large_grid():
    grid = [[1]*10 for _ in range(10)]  # 10x10 all ones
    # each row needs ceil(10/3)=4 buckets, 10 rows -> 40
    assert max_fill(grid, 3) == 40

# Ensure the function returns an integer

def test_return_type():
    grid = [[1,1],[1,1]]
    result = max_fill(grid, 2)
    assert isinstance(result, int)


def max_fill(grid, capacity):
    """
    Returns the number of times a bucket of the given capacity must be lowered
    to empty all wells represented by a grid of 0/1 values.

    Parameters
    ----------
    grid : List[List[int]]
        A list of rows, each containing 0s and 1s. ``1`` denotes one unit of
        water in the well corresponding to that row.
    capacity : int
        The capacity of each bucket. Must be >= 1 as per constraints.

    Returns
    -------
    int
        Total number of bucket lowers required.
    """
    if capacity <= 0:
        raise ValueError("capacity must be a positive integer")

    total_lowers = 0
    for row in grid:
        units = sum(row)
        # ceil division using integer arithmetic
        lowers = (units + capacity - 1) // capacity
        total_lowers += lowers
    return total_lowers

def test_check():


    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6, "Error"
    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5, "Error"
    assert max_fill([[0,0,0], [0,0,0]], 5) == 0, "Error"

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert max_fill([[1,1,1,1], [1,1,1,1]], 2) == 4, "Error"
    assert max_fill([[1,1,1,1], [1,1,1,1]], 9) == 2, "Error"

