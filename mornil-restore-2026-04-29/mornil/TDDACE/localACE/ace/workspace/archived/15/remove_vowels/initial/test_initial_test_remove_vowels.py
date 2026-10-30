import pytest\n\n@pytest.mark.parametrize("input_str,expected", [\n    ("", ""),\n    ("abcdef\nghijklm", "bcdf\nghjklm"),\n    ("abcdef", "bcdf"),\n    ("aaaaa", ""),\n    ("aaBAA", "B"),\n    ("zbcd", "zbcd"),\n    ("aeiouAEIOU", ""),\n    ("aA", ""),\n    ("Hello World", "Hll Wrld"),\n    ("Programming", "Prgrmmng"),\n    ("a\nA", "\n"),\n])\n\ndef test_remove_vowels(input_str, expected):\n    assert remove_vowels(input_str) == expected

def remove_vowels(text):
    """Return *text* with all vowels (aeiou, caseâinsensitive) removed."""
    vowels = "aeiouAEIOU"
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

