import pytest


# Parametric test covering the examples from the docstring
@pytest.mark.parametrize(
    "input_text,expected",
    [
        ("", ""),
        ("abcdef", "bcdf"),
        ("aaBAA", "B"),
        ("zbcd", "zbcd"),
        ("abcdef\nghijklm", "bcdf\nghjklm"),
    ],
)
def test_remove_vowels_examples(input_text, expected):
    assert remove_vowels(input_text) == expected


# Test with digits, punctuation and mixed case to ensure all nonâvowel characters are preserved

def test_remove_vowels_with_digits_and_punctuation():
    assert remove_vowels("123abc!") == "123bc!"


# Test that all vowels are removed when the input consists solely of vowels

def test_remove_vowels_all_vowels():
    assert remove_vowels("aeiouAEIOU") == ""


# Test that a mix of vowels and consonants retains case for consonants

def test_remove_vowels_case_preservation():
    assert remove_vowels("AppleBanana") == "pplBnn"


def remove_vowels(text):
    """
    Return a new string returned from text by removing all vowels.

    >>> remove_vowels('')
    ''
    >>> remove_vowels('abcdef
ghijklm')
    'bcdf
ghjklm'
    >>> remove_vowels('abcdef')
    'bcdf'
    >>> remove_vowels('aaaaa')
    ''
    >>> remove_vowels('aaBAA')
    'B'
    >>> remove_vowels('zbcd')
    'zbcd'
    """
    vowels = set('aeiouAEIOU')
    return ''.join(ch for ch in text if ch not in vowels)



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

