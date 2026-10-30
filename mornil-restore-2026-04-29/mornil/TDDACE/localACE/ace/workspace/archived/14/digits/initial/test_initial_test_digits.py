def test_digits_single_odd():
    assert digits(1) == 1


def test_digits_single_even():
    assert digits(4) == 0


def test_digits_multiple_digits():
    assert digits(235) == 15


def test_digits_all_even_digits():
    assert digits(2468) == 0


def test_digits_with_zero_and_odd_digits():
    assert digits(105) == 5


def test_digits_zero_only_even_digit():
    assert digits(2000) == 0


def test_digits_large_number():
    assert digits(99999999) == 9**8


def test_digits_mixed_even_odd_zero():
    assert digits(1203) == 3


def test_digits_first_and_last_digit_odd():
    assert digits(101) == 1


def test_digits_return_type():
    assert isinstance(digits(153), int)

def digits(n):
    """Return product of the odd digits of a positive integer.
    If all digits are even, return 0.
    """
    product = 1
    has_odd = False
    for ch in str(n):
        d = int(ch)
        if d % 2 == 1:
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

