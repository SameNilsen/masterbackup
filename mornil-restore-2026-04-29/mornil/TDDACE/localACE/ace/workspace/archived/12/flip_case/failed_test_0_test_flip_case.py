def test_flip_case_basic():
    assert flip_case('Hello') == 'hELLO'
    assert flip_case('abc') == 'ABC'
    assert flip_case('XYZ') == 'xyz'

def test_flip_case_non_alpha():
    assert flip_case('123!@') == '123!@'
    assert flip_case('Hello123') == 'hELLO123'

def test_flip_case_empty():
    assert flip_case('') == ''

def test_flip_case_unicode():
    assert flip_case('Ã±Ã¡B') == 'ÃÃb'

def test_flip_case_spaces():
    assert flip_case('Ab Cde F') == 'aB cDE f'

