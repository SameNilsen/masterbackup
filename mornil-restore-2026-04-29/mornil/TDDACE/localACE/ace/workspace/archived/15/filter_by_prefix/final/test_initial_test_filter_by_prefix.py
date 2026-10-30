import pytest


def test_filter_by_prefix_empty_input():
    # Empty input list should return an empty list
    assert filter_by_prefix([], "a") == []


def test_filter_by_prefix_matches():
    # Basic matching scenario
    data = ["abc", "bcd", "cde", "array"]
    assert filter_by_prefix(data, "a") == ["abc", "array"]


def test_filter_by_prefix_no_matches():
    # No string starts with the prefix
    data = ["b", "c"]
    assert filter_by_prefix(data, "a") == []


def test_filter_by_prefix_empty_prefix():
    # Prefix is empty string â should match all
    data = ["foo", "bar", "baz"]
    assert filter_by_prefix(data, "") == data


def test_filter_by_prefix_case_sensitivity():
    # Matching is caseâsensitive
    data = ["Abc", "aBc", "abc"]
    assert filter_by_prefix(data, "a") == ["abc"]


def test_filter_by_prefix_immutability():
    # The original list should not be modified
    original = ["abc", "abd", "acd"]
    copy = list(original)
    filter_by_prefix(original, "a")
    assert original == copy


def test_filter_by_prefix_long_prefix():
    # Prefix longer than any string should exclude those strings
    data = ["abc", "abcd", "abcde"]
    assert filter_by_prefix(data, "abcdef") == []


def test_filter_by_prefix_order_preserved():
    # Ensure the order of matches is preserved
    data = ["bcd", "abc", "acd", "acd1"]
    assert filter_by_prefix(data, "a") == ["abc", "acd", "acd1"]


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Return a new list containing only strings from *strings* that start with *prefix*.
    The order of the matching strings is preserved, and the original list remains
    unchanged.
    """
    return [s for s in strings if s.startswith(prefix)]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert filter_by_prefix([], 'john') == []
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

