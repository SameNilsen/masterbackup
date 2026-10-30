import pytest

# Helper to generate the correct Roman numeral for a given integer.
def _expected_roman(num: int) -> str:
    val_map = [
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
    for value, sym in val_map:
        count, num = divmod(num, value)
        result.append(sym * count)
    return "".join(result)

# 1. Known values, directly taken from the specification.
def test_known_values():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(4) == "iv"
    assert int_to_mini_roman(9) == "ix"
    assert int_to_mini_roman(19) == "xix"
    assert int_to_mini_roman(152) == "clii"
    assert int_to_mini_roman(426) == "cdxxvi"
    assert int_to_mini_roman(999) == "cmxcix"
    assert int_to_mini_roman(1000) == "m"

# 2. Parametrized tests for a representative set.
@pytest.mark.parametrize("value,expected", [
    (2, "ii"), (3, "iii"), (5, "v"), (6, "vi"), (7, "vii"),
    (8, "viii"), (10, "x"), (11, "xi"), (20, "xx"), (30, "xxx"),
    (40, "xl"), (50, "l"), (60, "lx"), (70, "lxx"), (80, "lxxx"),
    (90, "xc"), (100, "c"), (200, "cc"), (300, "ccc"), (400, "cd"),
    (500, "d"), (600, "dc"), (700, "dcc"), (800, "dccc"), (900, "cm"),
    (1000, "m"),
])
def test_parametrized_roman(value, expected):
    assert int_to_mini_roman(value) == expected

# 3. Full-range programmatic verification.
def test_programmatic_generation():
    for n in range(1, 1001):
        assert int_to_mini_roman(n) == _expected_roman(n)

# 4. Type validation checks.
def test_type_validation_error():
    with pytest.raises(TypeError):
        int_to_mini_roman("100")
    with pytest.raises(TypeError):
        int_to_mini_roman([100])
    with pytest.raises(TypeError):
        int_to_mini_roman(99.9)
    with pytest.raises(TypeError):
        int_to_mini_roman(True)  # bool is subclass of int

# 5. Outâofârange values.
def test_value_range_error():
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(-10)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)

# 6. Return type and case.
def test_return_type_and_case():
    result = int_to_mini_roman(53)
    assert isinstance(result, str)
    assert result.islower()

