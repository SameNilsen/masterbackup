def test_example1_max_fill():
    grid = [[0,0,1,0], [0,1,0,0], [1,1,1,1]]
    capacity = 1
    result = max_fill(grid, capacity)
    assert result == 6

def test_example2_max_fill():
    grid = [[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]]
    capacity = 2
    result = max_fill(grid, capacity)
    assert result == 5

def test_example3_max_fill():
    grid = [[0,0,0], [0,0,0]]
    capacity = 5
    result = max_fill(grid, capacity)
    assert result == 0

def test_exact_capacity():
    grid = [[1,1,1,1,1,1,1]]
    capacity = 7
    result = max_fill(grid, capacity)
    assert result == 1

def test_capacity_greater_than_total():
    grid = [[1,0,0]]
    capacity = 5
    result = max_fill(grid, capacity)
    assert result == 1

def test_large_grid_exact_division():
    grid = [[1]*100 for _ in range(100)]
    capacity = 10
    result = max_fill(grid, capacity)
    assert result == 1000

def test_single_well_zero_water():
    grid = [[0,0,0]]
    capacity = 3
    result = max_fill(grid, capacity)
    assert result == 0

def max_fill(grid, capacity):
    """Return the minimal number of bucket lowerings required to empty all wells.

    Parameters:
        grid (List[List[int]]): A 2D list where each inner list represents a well and
             contains 0s and 1s. Each 1 denotes one unit of water.
        capacity (int): The maximum number of water units that can be extracted
            with a single bucket lowering.

    Returns:
        int: Total number of bucket lowerings needed to empty all wells.
    """
    import math
    total_lowerings = 0
    for well in grid:
        units = sum(well)      # Count water units in this well.
        if units:              # Skip the ceil for zero units (results in 0).
            total_lowerings += math.ceil(units / capacity)
        # If units == 0, it contributes 0 to the total.
    return total_lowerings

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

