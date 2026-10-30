import pytest

# Test that simple space separated words are correctly split.

def test_split_spaces():
    assert words_string("Hi my name") == ["Hi", "my", "name"]

# Test that comma separated words, with optional space after comma, are correctly split.

def test_split_commas():
    assert words_string("One, two, three") == ["One", "two", "three"]

# Test that a mixture of commas and spaces is correctly split.

def test_split_mixed():
    assert words_string("Hi, my name is John") == ["Hi", "my", "name", "is", "John"]

# Test that leading/trailing whitespace and commas are ignored.

def test_strip_whitespace_and_commas():
    assert words_string("  One, two, three  ") == ["One", "two", "three"]

# Test that consecutive delimiters do not produce empty strings.

def test_consecutive_delimiters():
    assert words_string("One,,two") == ["One", "two"]
    assert words_string("  A  , B , C  ") == ["A", "B", "C"]

# Test that an empty string returns an empty list.

def test_empty_string():
    assert words_string("") == []

# Test that a string with only spaces returns an empty list.

def test_only_spaces():
    assert words_string("   ") == []

# Test that a string with only commas returns an empty list.

def test_only_commas():
    assert words_string(",,,") == []

# Test that multiple consecutive spaces are treated as a single delimiter.

def test_multiple_spaces():
    assert words_string("Hello  world") == ["Hello", "world"]


import re


def words_string(s: str) -> list[str]:
    s = s.strip(" ,")
    if not s:
        return []
    return [word for word in re.split(r'[,\s]+', s) if word]

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

