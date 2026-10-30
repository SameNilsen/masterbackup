def test_given_examples():
    assert max_fill([[0,0,1,0],[0,1,0,0],[1,1,1,1]], 1) == 6
    assert max_fill([[0,0,1,1],[0,0,0,0],[1,1,1,1],[0,1,1,1]], 2) == 5
    assert max_fill([[0,0,0],[0,0,0]], 5) == 0

def test_all_zones_empty():
    assert max_fill([[0,0,0],[0,0,0]], 1) == 0

def test_rounding():
    grid = [[1,1,1]]  # 3 units
    cap = 5
    assert max_fill(grid, cap) == 1

def test_mixed_rows():
    grid = [[1,1,1],[1,1,1,1,1,1,1,1,1,1]]  # 3 units and 10 units
    cap = 4
    expected = (3 + cap - 1)//cap + (10 + cap - 1)//cap
    assert max_fill(grid, cap) == expected

def test_large_grid_all_ones():
    grid = [[1]*10 for _ in range(10)]
    assert max_fill(grid, 3) == 40

def test_capacity_one():
    grid = [[1,0,1],[0,1,0]]
    expected = sum(sum(row) for row in grid)
    assert max_fill(grid, 1) == expected

def max_fill(grid, capacity):\n    

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

