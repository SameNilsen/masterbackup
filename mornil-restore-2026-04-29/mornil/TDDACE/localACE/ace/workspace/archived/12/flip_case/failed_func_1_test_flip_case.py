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

def flip_case(string: str) -> str:
    """
    Flip lowercase characters to uppercase and uppercase to lowercase.

    Example:
    >>> flip_case('Hello')
    'hELLO'
    """
    return string.swapcase()

