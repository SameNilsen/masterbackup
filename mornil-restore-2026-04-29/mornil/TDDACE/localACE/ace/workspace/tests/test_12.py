import pytest

# Assume `can_arrange` is defined in the same module or imported appropriately.

def test_can_arrange_empty():
    assert can_arrange([]) == -1

def test_can_arrange_single_element():
    assert can_arrange([42]) == -1

def test_can_arrange_descending_two():
    assert can_arrange([2, 1]) == 1

def test_can_arrange_descending_three():
    assert can_arrange([3, 2, 1]) == 2

@pytest.mark.parametrize(
    "arr,expected",
    [
        ([1, 4, 3, 2, 5], 3),      # multiple decreasing points, return largest index
        ([1, 2, 3, 4], -1),        # strictly increasing
        ([0, -1, -2, 3], 2),      # negative numbers
        ([1, 0, 2, 1, 3], 3),      # alternate pattern
        ([1, 2, 4, 3, 5], 3),      # example from docstring
        ([1, 2, 3], -1),          # example from docstring
    ],
)
def test_can_arrange_various(arr, expected):
    assert can_arrange(arr) == expected
