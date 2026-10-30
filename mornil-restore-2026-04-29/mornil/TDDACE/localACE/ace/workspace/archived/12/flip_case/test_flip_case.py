def test_empty_string():
    assert flip_case("") == ""

def test_all_lowercase():
    assert flip_case("abcd") == "ABCD"

def test_all_uppercase():
    assert flip_case("WXYZ") == "wxyz"

def test_mixed():
    assert flip_case("Hello World 123") == "hELLO wORLD 123"

def test_no_letters():
    assert flip_case("12345!@#") == "12345!@#"

def test_alphabet_circle():
    assert flip_case("abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ") == "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"

def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'

def test_flip_case_empty():
    assert flip_case('') == ''

def test_flip_case_mixed():
    assert flip_case('AbC123!') == 'aBc123!'

def test_flip_case_all_upper():
    assert flip_case('ALLUPPER') == 'allupper'

def test_flip_case_all_lower():
    assert flip_case('alllower') == 'ALLLOWER'

def test_flip_case_numbers_and_symbols():
    s = "!@#$%^&*()_+-=[]{}|;:,./<>?1234567890"
    assert flip_case(s) == s

def test_flip_case_whitespace_and_punctuation():
    input_str = 'Hello World! 123'
    expected = 'hELLO wORLD! 123'
    assert flip_case(input_str) == expected'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

import pytest


def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'


def test_flip_case_empty():
    assert flip_case('') == ''


def test_flip_case_all_caps():
    assert flip_case('TEST') == 'test'


def test_flip_case_all_lower():
    assert flip_case('test') == 'TEST'


def test_flip_case_mixed():
    assert flip_case('tHeiR') == 'THeir'


def test_flip_case_non_alpha():
    assert flip_case('1234!@#') == '1234!@#'


def test_flip_case_mixed_symbols():
    assert flip_case('Hello, WORLD! 123') == 'hELLO, world! 123'


def test_flip_case_unicode():
    # Unicode characters that have case; should flip if possible
    assert flip_case('ÏÎ Î±Î') == 'ÏÎ ÎÎ±'

def flip_case(string: str) -> str:
    """For a given string, flip lowercase letters to uppercase and uppercase letters to lowercase."""
    return string.swapcase()

