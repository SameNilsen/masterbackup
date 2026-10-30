def test_filter_by_prefix_empty_input():
    assert filter_by_prefix([], 'a') == []


def test_filter_by_prefix_docstring_example():
    assert filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a') == ['abc', 'array']


def test_filter_by_prefix_multiple_matches():
    strings = ['apple', 'application', 'apex', 'banana']
    assert filter_by_prefix(strings, 'app') == ['apple', 'application']


def test_filter_by_prefix_no_match():
    assert filter_by_prefix(['abc', 'bcd'], 'z') == []


def test_filter_by_prefix_case_sensitivity():
    strings = ['Apple', 'apricot', 'banana']
    # Only 'Apple' starts with an uppercase 'A'
    assert filter_by_prefix(strings, 'A') == ['Apple']


def test_filter_by_prefix_prefix_longer_than_strings():
    assert filter_by_prefix(['a', 'ab'], 'abc') == []


def test_filter_by_prefix_empty_prefix_matches_all():
    strings = ['foo', 'bar', 'baz']
    assert filter_by_prefix(strings, '') == ['foo', 'bar', 'baz']


def test_filter_by_prefix_original_list_unchanged():
    original = ['a', 'ab', 'c']
    copied = original[:]
    filter_by_prefix(original, 'a')
    assert original == copied, "The original list should remain unchanged"

from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    return [s for s in strings if s.startswith(prefix)]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert filter_by_prefix([], 'john') == []
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

