def test_flip_case_basic():
    assert flip_case("Hello") == "hELLO"

def test_flip_case_empty():
    assert flip_case("") == ""

def test_flip_case_all_lower():
    assert flip_case("abc") == "ABC"

def test_flip_case_all_upper():
    assert flip_case("ABC") == "abc"

def test_flip_case_mixed_alnum():
    assert flip_case("a1B2c3") == "A1b2C3"

def test_flip_case_unicode():
    # 'Ã' becomes 'SS', 'Ã' becomes 'Ã©', 'Ã¥' becomes 'Ã'
    assert flip_case("ÃÃÃ¥") == "SSÃ©Ã"

def test_flip_case_no_case_change():
    assert flip_case("12345") == "12345"

def test_flip_case_return_type():
    assert isinstance(flip_case("Hello"), str)


def flip_case(string: str) -> str:
    """ Flip the case of all alphabetic characters in string. """
    return string.swapcase()

METADATA = {
    'author': 'jt',
    'description': 'Swap case of a string'
}

def check(candidate):
    assert candidate('Hello') == 'hELLO'
    assert candidate('') == ''
    assert candidate('abc') == 'ABC'
    assert candidate('ABC') == 'abc'
    assert candidate('a1B2c3') == 'A1b2C3'
    assert candidate('ÃÂÃÂÃÂ¥') == 'SSÃÂ©ÃÂ'
    assert candidate('12345') == '12345'



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

