No final answer found

def int_to_mini_roman(number):\n    """\n    Convert a positive integer (1 <= number <= 1000) into its Roman numeral representation in lowercase.
\n    Parameters:\n    -----------\n    number : int\n        The integer to convert. Must be between 1 and 1000 inclusive.
\n    Returns:\n    --------\n    str\n        The Roman numeral representation in lowercase letters.
\n    Raises:\n    -------\n    TypeError\n        If *number* is not an instance of ``int``.
    ValueError\n        If *number* is outside the inclusive range [1, 1000].\n    """
    # Type validation â per playbook guidelines.
    if not isinstance(number, int):
        raise TypeError("Number must be an integer")

    # Range check.
    if number < 1 or number > 1000:
        raise ValueError("Number must be in the inclusive range 1 to 1000")

    # Map of Roman numeral symbols to their integer values, sorted in descending order.
    # Using the correct subtractive pairs.
    roman_pairs = [
        (1000, 'M'),
        (900,  'CM'),
        (500,  'D'),
        (400,  'CD'),
        (100,  'C'),
        (90,   'XC'),
        (50,   'L'),
        (40,   'XL'),
        (10,   'X'),
        (9,    'IX'),
        (5,    'V'),
        (4,    'IV'),
        (1,    'I')
    ]

    result = []
    remainder = number

    for value, symbol in roman_pairs:
        if remainder == 0:
            break
        count = remainder // value
        if count:
            result.append(symbol * count)
            remainder -= value * count

    return ''.join(result).lower()

def test_check():

    # Check some simple cases
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(251) == 'ccli'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(43) == 'xliii'
    assert int_to_mini_roman(90) == 'xc'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(532) == 'dxxxii'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(994) == 'cmxciv'
    assert int_to_mini_roman(1000) == 'm'

    # Check some edge cases that are easy to work out by hand.
    assert True





