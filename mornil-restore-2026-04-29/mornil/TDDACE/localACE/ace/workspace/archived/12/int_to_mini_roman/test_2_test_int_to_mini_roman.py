def test_int_to_mini_roman_basic():
    """Verify conversions for representative small values and subtractive pairs."""
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(40) == "xl"
    assert int_to_mini_roman(90) == "xc"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(426) == "cdxxvi"  # example from the description


def test_int_to_mini_roman_boundary_and_random():
    """Test boundary values, random nearâextreme numbers, and lowerâcase enforcement."""
    cases = {
        100: "c",
        500: "d",
        999: "cmxcix",
        1000: "m",
        77: "lxxvii",
        582: "dlxxxii"
    }
    for num, expected in cases.items():
        result = int_to_mini_roman(num)
        assert result == expected, f"{num} -> {result}, expected {expected}"
        assert result.islower(), f"Result for {num} is not lowerâcase: {result}"
        assert all(ch.isalpha() for ch in result), f"Nonâalphabetic characters in result for {num}: {result}"

def int_to_mini_roman(number: int) -> str:
    """Return the minimal Roman numeral of a positive integer 1â1000 in lowercase."""
    if number <= 0 or number > 1000:
        raise ValueError("Number out of allowed range: 1-1000")
    value_symbols = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'),
        (1, 'i')
    ]
    parts: list[str] = []
    for value, symbol in value_symbols:
        while number >= value:
            parts.append(symbol)
            number -= value
    return ''.join(parts)

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

