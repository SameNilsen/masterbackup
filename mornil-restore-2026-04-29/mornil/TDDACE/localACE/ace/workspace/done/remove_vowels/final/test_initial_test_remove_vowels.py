def _expected_no_vowels(text: str) -> str:
    """Return a copy of *text* with all vowels removed."""
    return ''.join(ch for ch in text if ch.lower() not in 'aeiou')


def test_remove_vowels_empty_string():
    assert remove_vowels('') == ''


def test_remove_vowels_basic():
    input_str = 'abcdef'
    expected = _expected_no_vowels(input_str)
    assert remove_vowels(input_str) == expected


def test_remove_vowels_all_vowels():
    input_str = 'aaaaa'
    expected = ''
    assert remove_vowels(input_str) == expected


def test_remove_vowels_mixed_case_vowels():
    input_str = 'aaBAA'
    expected = _expected_no_vowels(input_str)
    assert remove_vowels(input_str) == expected


def test_remove_vowels_no_vowels():
    input_str = 'zbcd'
    expected = 'zbcd'
    assert remove_vowels(input_str) == expected


def test_remove_vowels_newlines():
    input_str = 'abcdef
ghijklm'
    expected = _expected_no_vowels(input_str)
    assert remove_vowels(input_str) == expected


def test_remove_vowels_type_validation_non_string():
    # Passing a nonâstring should raise a TypeError when the function tries to iterate over it.
    try:
        remove_vowels(123)
    except TypeError:
        pass
    else:
        raise AssertionError('remove_vowels did not raise TypeError for nonâstring input')

def remove_vowels(text):
    """Return *text* with all vowels removed.

    Parameters
    ----------
    text : str
        Input string.

    Raises
    ------
    TypeError
        If *text* is not a string.

    Examples
    --------
    >>> remove_vowels('')
    ''
    >>> remove_vowels('abcdef\nghijklm')
    'bcdf\nghjklm'
    >>> remove_vowels('aaBAA')
    'B'
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")
    return ''.join(ch for ch in text if ch.lower() not in 'aeiou')



METADATA = {}


def test_check():
    assert remove_vowels('') == ''
    assert remove_vowels("abcdef
ghijklm") == 'bcdf
ghjklm'
    assert remove_vowels('fedcba') == 'fdcb'
    assert remove_vowels('eeeee') == ''
    assert remove_vowels('acBAA') == 'cB'
    assert remove_vowels('EcBOO') == 'cB'
    assert remove_vowels('ybcd') == 'ybcd'

