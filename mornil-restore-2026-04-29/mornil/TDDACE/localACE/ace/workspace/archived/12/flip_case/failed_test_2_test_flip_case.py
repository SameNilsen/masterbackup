def test_flip_case_docstring_example():
    assert flip_case('Hello') == 'hELLO'

def test_flip_case_all_uppercase():
    assert flip_case('HELLO') == 'hello'

def test_flip_case_all_lowercase():
    assert flip_case('hello') == 'HELLO'

def test_flip_case_mixed_case():
    assert flip_case('aBcD') == 'AbCd'

def test_flip_case_numbers_and_punctuation():
    assert flip_case('123!@#') == '123!@#'

def test_flip_case_mixed_alnum():
    assert flip_case('Ab12c') == 'aB12C'

def test_flip_case_empty_string():
    assert flip_case('') == ''

def test_flip_case_unicode():
    assert flip_case('ÃÃ¶Ã') == 'Ã¤ÃÃ¼'


