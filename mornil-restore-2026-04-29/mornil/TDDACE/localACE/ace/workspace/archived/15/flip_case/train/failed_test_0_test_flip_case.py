def test_flip_case_example():
    assert flip_case("Hello") == "hELLO"


def test_flip_case_all_upper():
    assert flip_case("ABCDEF") == "abcdef"


def test_flip_case_all_lower():
    assert flip_case("abcdef") == "ABCDEF"


def test_flip_case_mixed():
    assert flip_case("AbC") == "aBc"


def test_flip_case_nonalpha():
    assert flip_case("123!@#") == "123!@#"


def test_flip_case_empty():
    assert flip_case("") == ""

# Unicode alphabetic characters â case toggling should apply to alphabetic code points.
def test_flip_case_unicode():
    assert flip_case("Ã©ÃÃ¤Ã") == "ÃÃ©ÃÃ¤"


import pytest

@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("Hello", "hELLO"),
        ("ABC", "abc"),
        ("a", "A"),
        ("", ""),
        ("123", "123"),
    ],
)
def test_flip_case_param(input_str, expected):
    assert flip_case(input_str) == expected


