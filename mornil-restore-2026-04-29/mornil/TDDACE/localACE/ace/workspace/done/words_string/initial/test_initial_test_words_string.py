import pytest

@pytest.mark.parametrize(
    "input_str,expected",
    [
        ("Hi, my name is John", ["Hi", "my", "name", "is", "John"]),
        ("One, two, three, four, five, six", ["One", "two", "three", "four", "five", "six"]),
        ("Hello, world", ["Hello", "world"]),
        ("  Hello   world  ", ["Hello", "world"]),
        ("Hello,,world", ["Hello", "world"]),
        ("Hello, ,world", ["Hello", "world"]),
        ("Hello,,   ,World", ["Hello", "World"]),
        ("Hello,", ["Hello"]),
        ("", []),
        ("1,2,3 4", ["1", "2", "3", "4"]),
        (" , , ", []),
    ],
)
def test_words_string(input_str, expected):
    assert words_string(input_str) == expected


def words_string(s: str) -> list[str]:
    """Split a string into words separated by commas or whitespace.

    Consecutive separators are treated as a single delimiter, and any
    leading or trailing separators are ignored. Empty input returns an empty
    list.
    """
    import re

    # Handle the edge case where the input is None or has no characters
    if not s:
        return []

    # Strip surrounding whitespace so that trailing separators don't
    # produce empty tokens after the split.
    cleaned = s.strip()
    if not cleaned:
        return []

    # Split at one or more commas or whitespace characters
    parts = re.split(r'[\,\s]+', cleaned)

    # Filter out any empty strings that may arise
    return [p for p in parts if p]

def test_check():

    # Check some simple cases
    assert True, "This prints if this assert fails 1 (good for debugging!)"
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]
    assert words_string("One, two, three, four, five, six") == ["One", "two", "three", "four", "five", "six"]
    assert words_string("Hi, my name") == ["Hi", "my", "name"]
    assert words_string("One,, two, three, four, five, six,") == ["One", "two", "three", "four", "five", "six"]

    # Check some edge cases that are easy to work out by hand.
    assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert words_string("") == []
    assert words_string("ahmed     , gamal") == ["ahmed", "gamal"]

