import pytest


def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'


def test_flip_case_empty():
    assert flip_case('') == ''


def test_flip_case_no_letters():
    assert flip_case('123456') == '123456'


def test_flip_case_mixed():
    assert flip_case('A1b') == 'a1B'
    assert flip_case('aBc123') == 'AbC123'


@pytest.mark.parametrize('inp,out', [
    ('Ã', 'Ã¡'),
    ('Ã¡', 'Ã'),
    ('Ã¡b', 'ÃB'),
    ('ÃB', 'Ã¡b')
])

def test_flip_case_unicode(inp, out):
    assert flip_case(inp) == out


def test_flip_case_return_type():
    assert isinstance(flip_case('Hello'), str)


def test_flip_case_non_string():
    with pytest.raises(TypeError):
        flip_case(123)

    with pytest.raises(TypeError):
        flip_case(None)




METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'

def test_flip_case_basic():
    """Typical mixed alphabetic string."""
    assert flip_case('Hello') == 'hELLO'

def test_flip_case_empty():
    """Empty string should return empty.''""
    assert flip_case('') == ''

def test_flip_case_mixed_content():
    """String containing letters, digits and punctuation."""
    assert flip_case('aBc12') == 'AbC12'
    assert flip_case('Test! 123') == 'tEST! 123'

def test_flip_case_unicode():
    """Unicode alphabetic characters are correctly flipped."""
    assert flip_case('Ã±ÃbC') == 'ÃÃ¡Bc'

def test_flip_case_digits_only():
    """Digit strings should remain unchanged."""
    assert flip_case('12345') == '12345'



