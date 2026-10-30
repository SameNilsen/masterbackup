def test_add_basic_cases():
    """Test the add function with standard positive integer inputs."""
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def test_add_negative_and_zero():
    """Test add with negative numbers, zero, and a mixed sign case."""
    assert add(-2, -3) == -5
    assert add(-5, 5) == 0
    assert add(0, 0) == 0

def test_add_large_numbers():
    """Test add with very large integer inputs to ensure no overflow issues."""
    assert add(123456789, 987654321) == 1111111110

def test_add_result_type():
    """Verify that the result is always of type int."""
    result = add(10, 20)
    assert isinstance(result, int)

def add(x: int, y: int) -> int:
    """Return the arithmetic sum of two integers.

    Parameters
    ----------
    x, y : int
        Integers to add.

    Returns
    -------
    int
        The sum of ``x`` and ``y``.
    """
    return x + y



METADATA = {}


def test_check():
    import random

    assert add(0, 1) == 1
    assert add(1, 0) == 1
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(7, 5) == 12

    for i in range(100):
        x, y = random.randint(0, 1000), random.randint(0, 1000)
        assert add(x, y) == x + y

