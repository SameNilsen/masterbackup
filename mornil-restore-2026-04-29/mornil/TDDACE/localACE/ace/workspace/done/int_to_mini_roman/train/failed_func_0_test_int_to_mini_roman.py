def _expected_minroman(num: int) -> str:
    """Return the canonical lowercase Roman numeral for a valid integer 1Â â¤Â numÂ â¤Â 1000."""
    mapping = [
        (1000, "m"),
        (900,  "cm"),
        (500,  "d"),
        (400,  "cd"),
        (100,  "c"),
        (90,   "xc"),
        (50,   "l"),
        (40,   "xl"),
        (10,   "x"),
        (9,    "ix"),
        (5,    "v"),
        (4,    "iv"),
        (1,    "i"),
    ]
    result = []
    for value, roman in mapping:
        count, num = divmod(num, value)
        result.append(roman * count)
    return "".join(result)


def test_basic_cases():
    """Test the canonical Roman numerals for all base symbols."""
    assert int_to_mini_roman(1)   == "i"
    assert int_to_mini_roman(4)   == "iv"
    assert int_to_mini_roman(5)   == "v"
    assert int_to_mini_roman(9)   == "ix"
    assert int_to_mini_roman(10)  == "x"
    assert int_to_mini_roman(40)  == "xl"
    assert int_to_mini_roman(50)  == "l"
    assert int_to_mini_roman(90)  == "xc"
    assert int_to_mini_roman(100) == "c"
    assert int_to_mini_roman(400) == "cd"
    assert int_to_mini_roman(500) == "d"
    assert int_to_mini_roman(900) == "cm"
    assert int_to_mini_roman(1000)== "m"


def test_boundary_cases():
    """Ensure the implementation works on the extremes of the allowed range."""
    assert int_to_mini_roman(1)   == _expected_minroman(1)
    assert int_to_mini_roman(1000)== _expected_minroman(1000)


def test_random_cases():
    """Generate many random values within the valid range and verify consistency."""
    import random
    rng = random.Random(0)  # deterministic seed
    for _ in range(200):
        n = rng.randint(1, 1000)
        assert int_to_mini_roman(n) == _expected_minroman(n), f"Failed on {n}"


def test_invalid_inputs():
    """Verify that nonâinteger or outâofârange values raise ValueError."""
    import pytest
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(-5)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(ValueError):
        int_to_mini_roman(2000)
    # type checks
    with pytest.raises(TypeError):
        int_to_mini_roman("10")
    with pytest.raises(TypeError):
        int_to_mini_roman(10.5)
    with pytest.raises(TypeError):
        int_to_mini_roman(None)


import pytest


def _expected_roman(num):
    mapping = [
        (1000, 'm'), (900, 'cm'), (500, 'd'), (400, 'cd'),
        (100, 'c'), (90, 'xc'), (50, 'l'), (40, 'xl'),
        (10, 'x'), (9, 'ix'), (5, 'v'), (4, 'iv'), (1, 'i')
    ]
    result = []
    for val, sym in mapping:
        while num >= val:
            result.append(sym)
            num -= val
    return ''.join(result)


@pytest.mark.parametrize("num,expected", [
    (1, 'i'), (4, 'iv'), (5, 'v'), (9, 'ix'), (14, 'xiv'), (19, 'xix'),
    (40, 'xl'), (44, 'xliv'), (49, 'xlix'), (50, 'l'), (90, 'xc'),
    (99, 'xcix'), (400, 'cd'), (499, 'cdxcix'), (500, 'd'), (600, 'dc'),
    (750, 'dcl'), (777, 'dcclxxvii'), (900, 'cm'), (999, 'cmxcix'), (1000, 'm')
])
def test_int_to_mini_roman_basic(num, expected):
    assert int_to_mini_roman(num) == expected


@pytest.mark.parametrize("value", [None, 1.5, "10", [10], (10,), {10:10}])
def test_int_to_mini_roman_type_error(value):
    with pytest.raises(TypeError):
        int_to_mini_roman(value)


@pytest.mark.parametrize("value", [0, -1, 1001, 2000])
def test_int_to_mini_roman_value_error(value):
    with pytest.raises(ValueError):
        int_to_mini_roman(value)


def test_int_to_mini_roman_consistency():
    for n in range(1, 1001):
        assert int_to_mini_roman(n) == _expected_roman(n)

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





