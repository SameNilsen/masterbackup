import pytest

@pytest.mark.parametrize(
    "n,expected",
    [
        (1, 1),        # single odd digit
        (4, 0),        # single even digit
        (235, 15),     # mix of odd digits
        (2486, 0),     # all even digits
        (102, 1),      # odd digit with zeros
        (20, 0),       # only even digits including zero
        (13579, 945),  # all odd digits
    ],
)
def test_digits(n, expected):
    assert digits(n) == expected


def digits(n):
    """Return the product of the odd digits of a positive integer.
    Return 0 if all digits are even.
    """
    product = 1
    found_odd = False
    while n:
        d = n % 10
        if d % 2 == 1:
            product *= d
            found_odd = True
        n //= 10
    return product if found_odd else 0

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

