def test_filter_by_prefix_basic():
    result = filter_by_prefix(["abc", "bcd", "cde", "array"], "a")
    assert result == ["abc", "array"]


def test_filter_by_prefix_no_match():
    result = filter_by_prefix(["apple", "banana", "cherry"], "x")
    assert result == []


def test_filter_by_prefix_empty_prefix():
    input_list = ["melon", "kiwi"]
    result = filter_by_prefix(input_list, "")
    assert result == input_list


def test_filter_by_prefix_exact_match():
    result = filter_by_prefix(["single", "singleton", "none"], "singleton")
    assert result == ["singleton"]


def test_filter_by_prefix_case_sensitive():
    input_list = ["Apple", "apple", "APPLE"]
    result = filter_by_prefix(input_list, "a")
    assert result == ["apple"]


def test_filter_by_prefix_order_preserved():
    input_list = ["alpha", "beta", "gamma", "alphabet"]
    result = filter_by_prefix(input_list, "a")
    assert result == ["alpha", "alphabet"]


def test_filter_by_prefix_ensure_input_unchanged():
    input_list = ["aaa", "bbb", "aaa"]
    result = filter_by_prefix(input_list, "a")
    assert result == ["aaa", "aaa"]
    assert input_list == ["aaa", "bbb", "aaa"]

from typing import List
def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """ Filter an input list of strings only for ones that start with a given prefix.
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    if not isinstance(strings, list):
        raise TypeError("strings must be a list")
    if not isinstance(prefix, str):
        raise TypeError("prefix must be a string")
    if not all(isinstance(s, str) for s in strings):
        raise TypeError("all elements of strings must be strings")

    return [s for s in strings if s.startswith(prefix)]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert filter_by_prefix([], 'john') == []
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

