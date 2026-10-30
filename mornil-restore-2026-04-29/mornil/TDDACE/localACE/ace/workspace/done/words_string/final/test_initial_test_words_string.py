import re\nimport pytest\n\n# Helper function that mimics a correct implementation\n# Splits on commas or whitespace, removes empty pieces\n\ndef expected_words(s: str):\n    return [w for w in re.split(r'[\,\s]+', s) if w]\n\n# Test cases\n\ndef test_words_string_basic_spaces(words_string):\n    s = "Hi my name is John"\n    assert words_string(s) == expected_words(s)\n\n\ndef test_words_string_basic_commas(words_string):\n    s = "One,two,three,four,five,six"\n    assert words_string(s) == expected_words(s)\n\n\ndef test_words_string_mixed_separators(words_string):\n    s = "A, B C, D"\n    assert words_string(s) == expected_words(s)\n\n\ndef test_words_string_trailing_separators(words_string):\n    s = "   , ,Hello,,World, "\n    assert words_string(s) == expected_words(s)\n\n\ndef test_words_string_empty_string(words_string):\n    s = ""\n    assert words_string(s) == expected_words(s)\n\n\ndef test_words_string_type_error(words_string):\n    with pytest.raises(Exception):\n        words_string(123)\n

import re\n\n\n def words_string(s):\n    \"\"\"Split a string into words using commas or whitespace separators.\n\n    Parameters:\n    s (str): The input string containing words separated by commas or whitespace.\n\n    Returns:\n    list[str]: A list of nonâempty words.\n\n    Raises:\n    TypeError: If the input is not a string.\n    \"\"\"\n    if not isinstance(s, str):\n        raise TypeError("s must be a string")\n    # Split on one or more commas or whitespace characters and filter out empties\n    return [w for w in re.split(r"[\,\s]+", s) if w]"


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

