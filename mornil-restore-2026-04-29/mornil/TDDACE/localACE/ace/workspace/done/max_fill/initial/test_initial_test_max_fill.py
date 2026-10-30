def test_examples():
    assert max_fill([[0,0,1,0], [0,1,0,0], [1,1,1,1]], 1) == 6
    assert max_fill([[0,0,1,1], [0,0,0,0], [1,1,1,1], [0,1,1,1]], 2) == 5
    assert max_fill([[0,0,0], [0,0,0]], 5) == 0


def expected_lower_count(grid, capacity):
    return sum((sum(row) + capacity - 1) // capacity for row in grid)


def test_random_grids_and_capacity():
    import random
    for _ in range(20):
        rows = random.randint(1, 10)
        cols = random.randint(1, 10)
        grid = [[random.randint(0, 1) for _ in range(cols)] for _ in range(rows)]
        capacity = random.randint(1, 10)
        expected = expected_lower_count(grid, capacity)
        assert max_fill(grid, capacity) == expected


def test_capacity_larger_than_all_units():
    grid = [[1, 0, 1, 0], [0, 0, 0, 0], [1, 1, 1, 0]]
    capacity = 10  # larger than any unit count in a row
    # Two rows contain water, so result should be 2
    assert max_fill(grid, capacity) == 2


def test_capacity_one_equals_total_units():
    grid = [[1, 0], [0, 1]]
    capacity = 1
    assert max_fill(grid, capacity) == 2  # each unit requires a separate bucket lower


def test_one_row_fewer_units_than_capacity():
    grid = [[1, 1, 0, 1, 0, 0]]
    capacity = 5
    assert max_fill(grid, capacity) == 1


def test_all_zeros_grid():
    grid = [[0] * 5 for _ in range(5)]
    capacity = 3
    assert max_fill(grid, capacity) == 0


def test_maximum_constraints():
    grid = [[1] * 100 for _ in range(100)]  # 100x100 grid of ones
    capacity = 10
    # Each row has 100 units => ceil(100/10)=10 lowers per row
    # Total lowers = 100 rows * 10 lowers = 1000
    assert max_fill(grid, capacity) == 1000

def max_fill(grid, capacity):
    # Sum the number of lowers needed per row using integer arithmetic.
    return sum((sum(row) + capacity - 1) // capacity for row in grid)


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

