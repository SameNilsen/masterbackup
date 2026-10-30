import pytest

# Helper that implements the expected product logic, used only by the tests

def _expected_product(n: int) -> int:
    prod = 1
    has_odd = False
    for ch in str(n):
        d = int(ch)
        if d % 2:  # odd digit
            prod *= d
            has_odd = True
    return prod if has_odd else 0

# ---------------------------------------------------------------------------
# Basic functionality tests
# ---------------------------------------------------------------------------

def test_digits_single_odd():
    """A single odd digit should return that digit."""
    assert digits(7) == 7

def test_digits_single_even():
    """A single even digit should return 0 (no odd digits)."""
    assert digits(8) == 0

def test_digits_multiple_digits():
    """Mixed digits â product of odds only."""
    assert digits(123456) == _expected_product(123456)

def test_digits_all_even():
    """All digits even â result should be 0."""
    assert digits(46896) == 0

def test_digits_large_number():
    """Large integer to test conversion and looping over many digits."""
    large = 12345678901234567890
    assert digits(large) == _expected_product(large)

# ---------------------------------------------------------------------------
# Validation tests â ensure the function behaves correctly for invalid input
# ---------------------------------------------------------------------------

def test_digits_type_validation_string():
    """Passing a string should raise TypeError."""
    with pytest.raises(TypeError):
        digits("123")

def test_digits_type_validation_float():
    """Passing a float should raise TypeError."""
    with pytest.raises(TypeError):
        digits(123.0)


def digits(n):
    """Return the product of all odd digits of a positive integer.

    Parameters
    ----------
    n : int
        A positive integer.

    Returns
    -------
    int
        The product of all odd digits.  If there are no odd digits, returns 0.

    Raises
    ------
    TypeError
        If ``n`` is not an ``int``.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")

    product = 1
    has_odd = False
    for ch in str(n):
        digit = int(ch)
        if digit % 2:
            product *= digit
            has_odd = True
    return product if has_odd else 0

def test_check():

    # Check some simple cases
    assert digits(5) == 5
    assert digits(54) == 5
    assert digits(120) ==1
    assert digits(5014) == 5
    assert digits(98765) == 315
    assert digits(5576543) == 2625

    # Check some edge cases that are easy to work out by hand.
    assert digits(2468) == 0

