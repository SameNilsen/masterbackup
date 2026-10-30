def test_single_odd_digit():\n    assert digits(1) == 1\n\n\ndef test_single_even_digit():\n    assert digits(4) == 0\n\n\ndef test_mixed_digits():\n    assert digits(235) == 15\n\n\ndef test_all_even_digits():\n    assert digits(2468) == 0\n\n\ndef test_all_odd_digits():\n    assert digits(13579) == 945\n\n\ndef test_number_with_zero():\n    assert digits(101) == 1

def digits(n):
    """Return the product of the odd digits of a positive integer `n`.
    If `n` contains no odd digits, return 0.
    """
    product = 1
    has_odd = False
    while n:
        digit = n % 10
        if digit % 2 == 1:
            product *= digit
            has_odd = True
        n //= 10
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

