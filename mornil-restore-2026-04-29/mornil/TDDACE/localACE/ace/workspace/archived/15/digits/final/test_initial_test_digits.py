def test_digits_single_odd():
    assert digits(1) == 1


def test_digits_single_even():
    assert digits(4) == 0


def test_digits_multiple_odds():
    # 2, 3, 5 are odd => 2*3*5 = 30
    assert digits(235) == 15


def test_digits_mixed_zero_even():
    # 1 is odd, 0 and 2 are even => 1
    assert digits(102) == 1


def test_digits_all_even():
    # 2, 4, 8, 0 are all even => 0
    assert digits(2480) == 0


def test_digits_large_product():
    # 1 * 3 * 5 * 7 = 105
    assert digits(1357) == 105


def test_digits_only_ones():
    # 1 repeated many times always product of 1
    assert digits(1111111111) == 1


def test_digits_single_high_odd():
    # 9 is odd
    assert digits(9) == 9


def test_digits_multiple_mix():
    # digits: 1, 2, 3, 4, 5, 6, 7, 8, 9 => odds 1*3*5*7*9 = 945
    assert digits(123456789) == 945

def digits(n):
    """Return the product of the odd digits in a positive integer.

    Parameters
    ----------
    n : int
        A positive integer.

    Returns
    -------
    int
        Product of odd digits; 0 if the number has no odd digits.
    """
    product = 1
    has_odd = False
    for ch in str(n):
        d = int(ch)
        if d % 2 == 1:  # odd digit
            product *= d
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

