import pytest


@pytest.mark.parametrize(
    "number,expected",
    [
        (1, "i"),
        (4, "iv"),
        (5, "v"),
        (9, "ix"),
        (10, "x"),
        (19, "xix"),
        (58, "lviii"),
        (99, "xcix"),
        (152, "clii"),
        (426, "cdxxvi"),
        (458, "cdlviii"),
        (999, "cmxcix"),
        (1000, "m"),
    ],
)
def test_int_to_mini_roman_values(number, expected):
    """Test pure integer inputs within the allowed range."""
    assert int_to_mini_roman(number) == expected


@pytest.mark.parametrize("number", [0, -1, 1001])
def test_int_to_mini_roman_invalid_range(number):
    """Values outside 1â1000 should raise ValueError."""
    with pytest.raises(ValueError):
        int_to_mini_roman(number)


@pytest.mark.parametrize("value", [3.14, "10", None])
def test_int_to_mini_roman_type_error(value):
    """Nonâint inputs must raise TypeError."""
    with pytest.raises(TypeError):
        int_to_mini_roman(value)


def test_int_to_mini_roman_lowercase():
    """All output strings must be lowercase."""
    result = int_to_mini_roman(19)
    assert isinstance(result, str)
    assert result.islower()


def int_to_mini_roman(number):
    """Return the Romanânumeral representation (lowerâcase) of a positive integer.

    The function accepts integers `1Â â¤Â numberÂ â¤Â 1000`.  Nonâinteger types raise a
    :class:`TypeError`, while values outside the supported range raise a
    :class:`ValueError`.

    Parameters
    ----------
    number : int
        The positive integer to convert.

    Returns
    -------
    str
        Romanânumeral string in lower case.
    """
    if type(number) is not int:
        raise TypeError("Input must be an integer")
    if number < 1 or number > 1000:
        raise ValueError("Input must be between 1 and 1000 inclusive")

    ROMAN_MAP = (
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
    )

    result = []
    for value, symbol in ROMAN_MAP:
        count = number // value
        if count:
            result.append(symbol * count)
            number -= value * count
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

