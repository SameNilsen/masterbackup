import pytest

# Example tests based on the problem statement

def test_max_fill_examples():
    assert max_fill([[0, 0, 1, 0], [0, 1, 0, 0], [1, 1, 1, 1]], 1) == 6
    assert max_fill([[0, 0, 1, 1], [0, 0, 0, 0], [1, 1, 1, 1], [0, 1, 1, 1]], 2) == 5
    assert max_fill([[0, 0, 0], [0, 0, 0]], 5) == 0

# Edge cases and additional scenarios
@pytest.mark.parametrize(
    "grid, capacity, expected",
    [
        ( [[1, 1, 1, 0, 0, 1]], 2, 2 ),            # ceil(4/2)=2
        ( [[0, 0]], 1, 0 ),                       # no water
        ( [[1, 0, 0]], 10, 1 ),                   # capacity > water
        ( [[1] * 12], 5, 3 ),                    # ceil(12/5)=3
        ( [[1, 0, 1], [1, 0, 0], [0, 0, 0]], 3, 2 ),  # two wells need one lowering each
    ],
)
def test_max_fill_edge_cases(grid, capacity, expected):
    assert max_fill(grid, capacity) == expected

def max_fill(grid, capacity):
    """Return the total number of bucket lowerings needed to empty all wells.

    Each row of ``grid`` represents a well.  A value of 1 denotes a unit of
    water, and each bucket can hold ``capacity`` units from a single well.
    The number of lowerings for a well with ``s`` units is the ceiling of
    ``s / capacity``.  The function sums this value over all wells.

    Args:
        grid: List of lists of int, where each inner list is a well.
        capacity: Positive int bucket capacity.

    Returns:
        int: Total number of bucket lowerings.
    """
    total = 0
    for well in grid:
        s = sum(well)
        if s:
            total += (s + capacity - 1) // capacity
    return total


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

