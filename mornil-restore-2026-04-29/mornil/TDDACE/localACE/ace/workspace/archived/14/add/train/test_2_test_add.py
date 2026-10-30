def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 7) == 12

def test_add_zero():
    assert add(0, 0) == 0
    assert add(0, 5) == 5
    assert add(5, 0) == 5

def test_add_negative_numbers():
    assert add(-5, -7) == -12
    assert add(-10, -15) == -25

def test_add_mixed_sign_numbers():
    assert add(-5, 10) == 5
    assert add(10, -5) == 5

def test_add_large_integers():
    large_a = 123456789012345678901234567890
    large_b = 987654321098765432109876543210
    assert add(large_a, large_b) == large_a + large_b

def test_add_result_type():
    result = add(2, 3)
    assert isinstance(result, int)


def add(x: int, y: int) -> int:
    """Return the sum of *x* and *y*.

    Parameters
    ----------
    x : int
        First operand.
    y : int
        Second operand.

    Returns
    -------
    int
        The arithmetic sum of the two operands.
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

