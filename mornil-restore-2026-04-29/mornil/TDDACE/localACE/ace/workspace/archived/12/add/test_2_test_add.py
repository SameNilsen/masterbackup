def test_add_basic() -> None:
    """Test the provided examples and simple addition."""
    assert add(2, 3) == 5
    assert add(5, 7) == 12


def test_add_negative() -> None:
    """Test addition with negative operands."""
    assert add(-5, -7) == -12
    assert add(-5, 7) == 2


def test_add_zero() -> None:
    """Test scenarios involving zero."""
    assert add(0, 0) == 0
    assert add(5, 0) == 5


def test_add_large_numbers() -> None:
    """Test handling of large integer values."""
    assert add(123456789, 987654321) == 1111111110


def test_add_return_type() -> None:
    """Ensure the function returns an integer instance."""
    assert isinstance(add(2, 3), int)


def test_add_returns_value() -> None:
    """Check that the function does return something (i.e., not None)."""
    assert add(1, 2) is not None

def add(x: int, y: int) -> int:
    """Add two numbers x and y
    >>> add(2, 3)
    5
    >>> add(5, 7)
    12
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

