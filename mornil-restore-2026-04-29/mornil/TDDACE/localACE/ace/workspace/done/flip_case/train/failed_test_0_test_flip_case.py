import pytest


# Helper function to generate the expected result by toggling case

def _expected_flip(string: str) -> str:
    return ''.join(c.upper() if c.islower() else c.lower() for c in string)


def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'


def test_flip_case_empty():
    assert flip_case('') == ''


def test_flip_case_all_lowercase():
    s = 'abcdefg'
    expected = s.upper()
    assert flip_case(s) == expected


def test_flip_case_all_uppercase():
    s = 'ABCDEFG'
    expected = s.lower()
    assert flip_case(s) == expected


def test_flip_case_mixed():
    s = 'AbC123!d'
    expected = _expected_flip(s)
    assert flip_case(s) == expected


def test_flip_case_unicode():
    s = 'Ã±ÃÃ§'
    expected = _expected_flip(s)
    assert flip_case(s) == expected


def test_flip_case_non_string():
    with pytest.raises(TypeError):
        flip_case(123)
    with pytest.raises(TypeError):
        flip_case(['a', 'b'])
    with pytest.raises(TypeError):
        flip_case(None)


