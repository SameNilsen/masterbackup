def expected_flip_case(s):
    return ''.join(ch.upper() if ch.islower() else ch.lower() if ch.isupper() else ch for ch in s)


def test_flip_case_basic():
    input_str = 'Hello'
    assert flip_case(input_str) == expected_flip_case(input_str)


def test_flip_case_all_lower():
    input_str = 'python'
    assert flip_case(input_str) == expected_flip_case(input_str)


def test_flip_case_all_upper():
    input_str = 'PYTHON'
    assert flip_case(input_str) == expected_flip_case(input_str)


def test_flip_case_mixed_and_non_letter():
    input_str = 'A1b!C2d'
    assert flip_case(input_str) == expected_flip_case(input_str)


def test_flip_case_empty():
    input_str = ''
    assert flip_case(input_str) == expected_flip_case(input_str)


def test_flip_case_unicode():
    input_str = 'Ã©ÃÃÆ©'
    assert flip_case(input_str) == expected_flip_case(input_str)


def test_flip_case_boundaries():
    input_str = 'aA'
    assert flip_case(input_str) == expected_flip_case(input_str)

def flip_case(string: str) -> str:
    """For a given string, flip lowercase characters to uppercase and uppercase to lowercase.

    >>> flip_case('Hello')
    'hELLO'
    """
    if not isinstance(string, str):
        raise TypeError("input must be a string")
    return "".join(
        ch.upper() if ch.islower() else ch.lower() if ch.isupper() else ch
        for ch in string
    )



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert flip_case('') == ''
    assert flip_case('Hello!') == 'hELLO!'
    assert flip_case('These violent delights have violent ends') == 'tHESE VIOLENT DELIGHTS HAVE VIOLENT ENDS'




