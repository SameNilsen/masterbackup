import pytest

# Test against the example cases provided in the docstring
@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
    ],
)
def test_cycpattern_examples(a, b, expected):
    assert cycpattern_check(a, b) is expected

# Positive cases where b itself is already a substring of a
@pytest.mark.parametrize(
    "a,b",
    [
        ("foobar", "bar"),
        ("abcabc", "abc"),
        ("single", "single"),
    ],
)
def test_cycpattern_substring(a, b):
    assert cycpattern_check(a, b) is True

# Positive cases where a rotation of b appears in a
@pytest.mark.parametrize(
    "a,b",
    [
        ("mississippi", "upss"),      # rotation "ssup"
        ("circular", "larci"),        # rotation "larci"
        ("kitchen", "ench"),          # rotation "ench"
    ],
)
def test_cycpattern_rotation_match(a, b):
    assert cycpattern_check(a, b) is True

# Negative cases â no rotation of b is a substring of a
@pytest.mark.parametrize(
    "a,b",
    [
        ("abcdefgh", "xyz"),
        ("same", "ames"),          # rotation "ames" is not in "same"
        ("testing", "tsting"),     # missing a character
    ],
)
def test_cycpattern_no_match(a, b):
    assert cycpattern_check(a, b) is False

# Edge cases involving empty strings
@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("", "", True),       # empty string is a substring of itself
        ("abc", "", True),    # empty string always a substring
        ("", "abc", False),   # nonâempty string cannot be substring of empty
    ],
)
def test_cycpattern_empty_strings(a, b, expected):
    assert cycpattern_check(a, b) is expected

# Verify the return type is always a boolean
@pytest.mark.parametrize(
    "a,b",
    [
        ("test", "est"),
        ("example", "amp"),
        ("empty", "e"),
    ],
)
def test_cycpattern_return_type(a, b):
    result = cycpattern_check(a, b)
    assert isinstance(result, bool)


