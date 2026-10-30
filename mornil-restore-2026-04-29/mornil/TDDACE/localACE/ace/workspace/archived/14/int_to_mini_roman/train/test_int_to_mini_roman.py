def test_int_to_mini_roman_examples():
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"


def test_int_to_mini_roman_edge_cases():
    # Lower boundary
    assert int_to_mini_roman(1) == "i"
    # Upper boundary
    assert int_to_mini_roman(1000) == "m"
    # Verify return type and basic conversion
    result = int_to_mini_roman(500)
    assert isinstance(result, str)
    assert result == "d"


def test_int_to_mini_roman_various_values():
    # Small numbers
    for n in [2, 3, 4, 9, 10, 14, 20]:
        # We precompute expected values manually
        expected = {2: "ii", 3: "iii", 4: "iv", 9: "ix", 10: "x", 14: "xiv", 20: "xx"}[n]
        assert int_to_mini_roman(n) == expected

    # Large numbers
    for n in [944, 357, 881]:
        # Manual expectations from Roman rules
        manual_expectations = {
            944: "cmxliv",
            357: "ccclvii",
            881: "dccclxxxi"
        }
        assert int_to_mini_roman(n) == manual_expectations[n]

def int_to_mini_roman(number: int) -> str:
    """Return the Roman numeral representation of *number* in lowercase.

    The function supports integers in the inclusive range 1â1000, using the
    standard subtractive Roman numerals.

    Parameters
    ----------
    number : int
        A positive integer between 1 and 1000.

    Returns
    -------
    str
        The Roman numeral string in lowercase.

    Examples
    --------
    >>> int_to_mini_roman(19)
    'xix'
    >>> int_to_mini_roman(152)
    'clii'
    >>> int_to_mini_roman(426)
    'cdxxvi'
    """
    # Mapping of integer values to Roman symbols, ordered descending
    value_symbols = [
        (1000, "M"),
        (900,  "CM"),
        (500,  "D"),
        (400,  "CD"),
        (100,  "C"),
        (90,   "XC"),
        (50,   "L"),
        (40,   "XL"),
        (10,   "X"),
        (9,    "IX"),
        (5,    "V"),
        (4,    "IV"),
        (1,    "I"),
    ]

    roman_parts = []
    remaining = number
    for value, symbol in value_symbols:
        while remaining >= value:
            roman_parts.append(symbol)
            remaining -= value
    return "".join(roman_parts).lower()

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

