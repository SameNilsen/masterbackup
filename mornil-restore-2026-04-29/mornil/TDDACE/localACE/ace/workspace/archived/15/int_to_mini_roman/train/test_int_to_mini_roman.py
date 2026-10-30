def test_single_digits_and_subtractive_notation():
    """Verify numbers 1â9, including subtractive notation."""
    mapping = {
        1: "i",
        2: "ii",
        3: "iii",
        4: "iv",
        5: "v",
        6: "vi",
        7: "vii",
        8: "viii",
        9: "ix",
    }
    for num, expected in mapping.items():
        assert int_to_mini_roman(num) == expected, f"Failed for {num}"


def test_tens_and_hundreds_subtractive_notation():
    """Check the subtractive forms for tens and hundreds."""
    cases = {
        40: "xl",
        90: "xc",
        400: "cd",
        900: "cm",
    }
    for num, expected in cases.items():
        assert int_to_mini_roman(num) == expected, f"Failed for {num}"


def test_boundary_cases():
    """Confirm the smallest and largest valid numbers."""
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"


def test_examples():
    """Validate the example cases provided in the docstring."""
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"


def test_combined_numbers():
    """Test several composite numbers to ensure correct string assembly."""
    cases = {
        233: "ccxxxiii",
        512: "dxii",
        798: "dccxcviii",
        999: "cmxcix",
    }
    for num, expected in cases.items():
        assert int_to_mini_roman(num) == expected, f"Failed for {num}"


def test_output_is_lowercase():
    """Make sure the returning string is in lowercase."""
    for num in [1, 4, 19, 152, 426, 999, 1000]:
        result = int_to_mini_roman(num)
        assert result.islower(), f"Result {result} is not lowercase"


def test_return_type():
    """The function must return a string type."""
    for num in [5, 100, 777]:
        assert isinstance(int_to_mini_roman(num), str)


def int_to_mini_roman(number: int) -> str:
    """Return the Roman numeral representation of an integer in lowercase.

    Args:
        number: an integer 1 <= number <= 1000.

    Returns:
        A string containing the Roman numeral in lowercase.

    Raises:
        ValueError: if number is outside the supported range.
    """
    if number < 1 or number > 1000:
        raise ValueError("number must be between 1 and 1000 inclusive")

    roman_map = [
        (1000, "m"),
        (900, "cm"),
        (500, "d"),
        (400, "cd"),
        (100, "c"),
        (90, "xc"),
        (50, "l"),
        (40, "xl"),
        (10, "x"),
        (9, "ix"),
        (5, "v"),
        (4, "iv"),
        (1, "i"),
    ]

    result = []
    for value, symbol in roman_map:
        while number >= value:
            result.append(symbol)
            number -= value
    return "".join(result)


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

