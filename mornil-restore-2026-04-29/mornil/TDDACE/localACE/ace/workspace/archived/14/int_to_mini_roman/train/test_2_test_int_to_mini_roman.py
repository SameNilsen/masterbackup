import pytest


def test_int_to_mini_roman_basic_cases():
    """Verify known mappings, including subtractive forms and boundaries."""
    cases = {
        1: 'i',
        4: 'iv',
        5: 'v',
        9: 'ix',
        10: 'x',
        19: 'xix',
        20: 'xx',
        40: 'xl',
        50: 'l',
        90: 'xc',
        100: 'c',
        152: 'clii',
        400: 'cd',
        426: 'cdxxvi',
        500: 'd',
        900: 'cm',
        1000: 'm',
    }
    for number, expected in cases.items():
        assert int_to_mini_roman(number) == expected


def test_int_to_mini_roman_value_out_of_range_should_raise():
    """Numbers outside 1â1000 must raise ValueError."""
    for invalid in (0, -5, 1001, 2000):
        with pytest.raises(ValueError, match="1 <= num <= 1000"):
            int_to_mini_roman(invalid)


def test_int_to_mini_roman_output_type_and_lowercase():
    """Check return type is str and output is lowerâcased."""
    example = 19
    result = int_to_mini_roman(example)
    assert isinstance(result, str)
    assert result == result.lower()  # ensure lowerâcasing
    assert result == 'xix'


def test_int_to_mini_roman_non_int_input():
    """Optional guard test: nonâintegers should raise TypeError if implemented."""
    for invalid in ('10', 5.5, None):
        with pytest.raises(TypeError):
            int_to_mini_roman(invalid)

def int_to_mini_roman(number):
    """Convert a positive integer (1 â¤ number â¤ 1000) to a Roman numeral in lowercase.

    Parameters
    ----------
    number : int
        Integer value to convert. Must lie in the inclusive range 1â¦1000.

    Returns
    -------
    str
        Roman numeral representation in lower case.

    Raises
    ------
    TypeError
        If ``number`` is not an ``int``.
    ValueError
        If ``number`` is outside 1â¦1000.
    """

    # Guard against nonâinteger inputs
    if not isinstance(number, int):
        raise TypeError("int_to_mini_roman expects an int")

    # Guard against outâofârange values
    if number < 1 or number > 1000:
        raise ValueError("1 <= num <= 1000")

    # Mapping of values to Roman symbols, including subtractive forms
    mapping = [
        (1000, "M"), (900, "CM"), (500, "D"), (400, "CD"),
        (100, "C"), (90, "XC"), (50, "L"), (40, "XL"),
        (10, "X"), (9, "IX"), (5, "V"), (4, "IV"), (1, "I")
    ]

    result = []
    for value, symbol in mapping:
        while number >= value:
            result.append(symbol)
            number -= value

    # Join symbols and lowerâcase the result as required
    return "".join(result).lower()

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

