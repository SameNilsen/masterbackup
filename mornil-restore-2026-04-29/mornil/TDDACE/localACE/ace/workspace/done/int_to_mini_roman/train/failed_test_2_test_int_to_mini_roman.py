import pytest

# Helper that reproduces the expected miniâroman string for a given number.
# It mirrors the logic that the implementation is supposed to follow.
# This keeps the expected values consistent and avoids manual mistakes.

def _expected_minroman(n: int) -> str:
    thousands = {0: "", 1: "m"}
    hundreds = {
        0: "", 1: "c", 2: "cc", 3: "ccc",
        4: "cd", 5: "d", 6: "dc", 7: "dcc", 8: "dccc", 9: "cm"
    }
    tens = {
        0: "", 1: "x", 2: "xx", 3: "xxx",
        4: "xl", 5: "l", 6: "lx", 7: "lxx", 8: "lxxx", 9: "xc"
    }
    ones = {
        0: "", 1: "i", 2: "ii", 3: "iii",
        4: "iv", 5: "v", 6: "vi", 7: "vii", 8: "viii", 9: "ix"
    }
    return (
        thousands[n // 1000]
        + hundreds[(n % 1000) // 100]
        + tens[(n % 100) // 10]
        + ones[n % 10]
    )

# ---------- Singleâdigit tests ----------

def test_single_digits():
    for num in [1, 4, 5, 9]:
        assert int_to_mini_roman(num) == _expected_minroman(num)

# ---------- Twoâdigit tests (additive and subtractive) ----------

def test_tens_subtractive_cases():
    cases = {
        14: "xiv",
        19: "xix",
        40: "xl",
        49: "xlix",
        90: "xc",
        99: "xcix",
    }
    for num, expected in cases.items():
        assert int_to_mini_roman(num) == expected

# ---------- Threeâdigit tests ----------

def test_hundreds_cases():
    cases = {
        100: "c",
        400: "cd",
        500: "d",
        900: "cm",
        499: "cdxcix",
        800: "dccc",
        321: "cccxxi",
    }
    for num, expected in cases.items():
        assert int_to_mini_roman(num) == expected

# ---------- Combination tests ----------

def test_combined_numbers():
    cases = {
        152: "clii",
        426: "cdxxvi",
        777: "dccclvii",
        999: "cmxcix",
    }
    for num, expected in cases.items():
        assert int_to_mini_roman(num) == expected

# ---------- Boundary tests ----------

def test_boundary_values():
    assert int_to_mini_roman(1) == "i"
    assert int_to_mini_roman(1000) == "m"

# ---------- Caseâsensitivity test ----------

def test_output_is_lowercase():
    for num in [1, 4, 19, 152, 426, 999, 1000]:
        result = int_to_mini_roman(num)
        assert result == result.lower(), f"Result {result} is not lowercase"


