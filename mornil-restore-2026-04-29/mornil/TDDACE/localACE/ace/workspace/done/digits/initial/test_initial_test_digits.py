import pytest

# Test the product of odd digits for various inputs, ensuring zeros are ignored and
# the function returns 0 when all digits are even.

@pytest.mark.parametrize("n, expected", [
    (1, 1),          # single odd digit
    (5, 5),          # single odd digit
    (4, 0),          # single even digit
    (14, 1),         # mix, only 1 odd digit
    (235, 15),       # mix, product of 3 and 5
    (2468, 0),       # all even digits
    (272, 7),        # one odd digit among evens
    (777, 343),      # repeated odd digits
    (101, 1),        # odd digits with zeros
    (1010, 1),       # zeros and odd digits
    (246912, 9),     # mix, product of 9 and 1
    (852864, 0),     # all even digits
    (10, 1),         # even followed by odd zero
    (20, 0),         # two evens
    (111, 1),        # repeated odd digits 1
    (135, 15),       # product 1*3*5
])
def test_digits_product_of_odds(n, expected):
    assert digits(n) == expected


def digits(n):
    """Return the product of the odd digits of a positive integer.
    If there are no odd digits, return 0.

    Parameters
    ----------
    n : int
        A positive integer.

    Returns
    -------
    int
        Product of odd digits or 0 when all digits are even.
    """
    product = 1
    found_odd = False
    for ch in str(n):
        d = int(ch)
        if d % 2 == 1:
            product *= d
            found_odd = True
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

