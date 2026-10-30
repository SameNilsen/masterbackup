import pytest

# Helper that reproduces the intended caseâflip logic

def _expected_flip(s: str) -> str:
    return "".join(
        c.upper() if c.islower() else c.lower() if c.isupper() else c
        for c in s
    )


def test_flip_case_basic():
    assert flip_case("Hello") == _expected_flip("Hello")


def test_flip_case_nonalpha():
    # Characters that are not letters should remain unchanged
    assert flip_case("123!@#") == _expected_flip("123!@#")


def test_flip_case_unicode():
    # Verify behaviour with Unicode letters
    assert flip_case("cafÃ©") == _expected_flip("cafÃ©")


def test_flip_case_empty_string():
    assert flip_case("") == _expected_flip("")


def test_flip_case_type_validation():
    # The function is expected to accept only strings; passing another type should raise TypeError
    with pytest.raises(TypeError):
        flip_case(123)


import pytest
from __main__ import flip_case


def expected_flip_case(s):
    return ''.join([c.lower() if c.isupper() else c.upper() for c in s])


def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('') == ''


def test_flip_case_mixed_and_numbers():
    s = 'HeLLo world! 123'
    assert flip_case(s) == expected_flip_case(s)


def test_flip_case_whitespace_and_punctuation():
    s = '  ABC-123 '
    assert flip_case(s) == expected_flip_case(s)


def test_flip_case_unicode():
    s = 'StraÃe'
    assert flip_case(s) == expected_flip_case(s)


def test_flip_case_non_string():
    with pytest.raises(AttributeError):
        flip_case(123)
    with pytest.raises(AttributeError):
        flip_case(['a', 'b'])


def test_flip_case_new_string_object():
    s = 'Test'
    result = flip_case(s)
    assert result is not s
    assert result != s



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'






def flip_case(string: str) -> str:
    """Return a new string with uppercase and lowercase letters exchanged.

    Args:
        string: The input string to transform.

    Returns:
        A new string with all alphabetic characters inverted in case.

    Raises:
        TypeError: If the input is not a string.

    Examples:
        >>> flip_case('Hello')
        'hELLO'
        >>> flip_case('hELLO')
        'Hello'
    """
    if not isinstance(string, str):
        raise TypeError("flip_case expects a string")
    return string.swapcase()

