No final answer found

def max_fill(grid, capacity):
    """
    Return the total number of times a bucket needs to be lowered to empty all wells.

    Parameters
    ----------
    grid : list[list[int]]
        Each inner list represents a row/hole. Each element is 0 or 1.
    capacity : int
        Capacity of each bucket.

    Returns
    -------
    int
        Total bucket lowers required.
    """
    # Type and value validation
    if not isinstance(grid, list) or not all(isinstance(r, list) for r in grid):
        raise TypeError("grid must be a list of lists")
    if not isinstance(capacity, int):
        raise TypeError("capacity must be an integer")
    if capacity < 1 or capacity > 10:
        raise ValueError("capacity must be in range 1..10")

    # Optional: check that all rows have the same length
    row_lengths = {len(r) for r in grid}
    if len(row_lengths) > 1:
        raise ValueError("all rows in the grid must have the same length")

    total_lowers = 0
    for row in grid:
        if any(cell not in (0, 1) for cell in row):
            raise ValueError("grid should contain only 0 or 1 values")
        ones = sum(row)
        if ones:
            # ceil division: (ones + capacity - 1) // capacity
            total_lowers += (ones + capacity - 1) // capacity
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

