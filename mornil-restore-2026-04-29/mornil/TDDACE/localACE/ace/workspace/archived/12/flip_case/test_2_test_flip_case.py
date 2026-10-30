def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'

def test_flip_case_lowercase():
    assert flip_case('abc') == 'ABC'

def test_flip_case_uppercase():
    assert flip_case('XYZ') == 'xyz'

def test_flip_case_mixed():
    assert flip_case('AbC') == 'aBc'

def test_flip_case_nonletters():
    assert flip_case('123!@#') == '123!@#'

def test_flip_case_unicode():
    assert flip_case('Ã±ÃÃ¤Ã') == 'ÃÃ±ÃÃ¤'

def test_flip_case_empty():
    assert flip_case('') == ''

def flip_case(string: str) -> str:
    """Return a copy of *string* with all uppercase letters converted to lowercase and vice versa."""
    return string.swapcase()




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

