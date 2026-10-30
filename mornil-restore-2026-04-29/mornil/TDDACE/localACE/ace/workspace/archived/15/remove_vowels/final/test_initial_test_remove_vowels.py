def test_empty_string():
    assert remove_vowels('') == ''


def test_single_line_without_newlines():
    assert remove_vowels('abcdef') == 'bcdf'


def test_multi_line():
    assert remove_vowels('abcdef\nghijklm') == 'bcdf\nghjklm'


def test_only_vowels():
    assert remove_vowels('aaaaa') == ''


def test_case_sensitive_vowels():
    # Upperâcase vowels should also be removed.
    assert remove_vowels('aaBAA') == 'B'


def test_no_vowels():
    assert remove_vowels('zbcd') == 'zbcd'


def test_preserve_non_vowel_chars():
    # Numbers, punctuation, and spaces must remain.
    assert remove_vowels('123, a! e? i? O??') == '123, !? ? ??'


def test_preserve_newlines_in_output():
    # Newlines must be preserved.
    assert remove_vowels('a\nb') == '\nb'


def test_uppercase_letters():
    # All uppercase vowels should be stripped.
    assert remove_vowels('BANANA') == 'BNN'


def test_mixed_case_and_punctuation():
    assert remove_vowels('HELLO WORLD!') == 'HLL WRLD!'


def remove_vowels(text):
    """Return *text* with all vowels removed.

    Vowels include both uppercase and lowercase characters: a, e, i, o, u.
    All other characters (punctuation, digits, spaces, newlines) are preserved.
    """
    vowels = "aeiouAEIOU"
    result = []
    for ch in text:
        if ch in vowels:
            continue
        result.append(ch)
    return ''.join(result)



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

