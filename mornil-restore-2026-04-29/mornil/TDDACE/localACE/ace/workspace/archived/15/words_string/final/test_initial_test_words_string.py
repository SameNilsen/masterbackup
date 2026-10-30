def test_words_string_comma_space():
    s = "Hi, my name is John"
    assert words_string(s) == ["Hi", "my", "name", "is", "John"]


def test_words_string_multiple_commas():
    s = "One, two, three, four, five, six"
    assert words_string(s) == ["One", "two", "three", "four", "five", "six"]


def test_words_string_multiple_separators():
    s = "Hello,, World  test"
    expected = ["Hello", "World", "test"]
    assert words_string(s) == expected


def test_words_string_edge_cases():
    assert words_string("") == []
    assert words_string(", , ,") == []
    assert words_string("   ") == []


def words_string(s):
    import re
    if not s:
        return []
    parts = re.split(r'[,\s]+', s.strip())
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

