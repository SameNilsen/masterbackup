"""
import pytest

# ---------------------------------------------------------------------------
# Test suite for the ``filter_by_prefix`` function
# ---------------------------------------------------------------------------

# 1. Basic functionality (matches the doctests from the implementation)
@pytest.mark.parametrize(
    "strings,prefix,expected",
    [
        ([], 'a', []),  # Empty input list
        (["abc", "bcd", "cde", "array"], 'a', ["abc", "array"]),  # Typical case
        (["ABC", "abcd", "abca"], "ab", ["abcd", "abca"]),  # Caseâsensitive match
        (["abc", "bcd", "cde"], "", ["abc", "bcd", "cde"]),  # Empty prefix returns all
        (["short", "tiny", "example"], "x", []),  # No matches at all
        (["some", "some"], "some", ["some", "some"]),  # Exact match and duplicates
    ],
)
def test_filter_by_prefix_basic(strings, prefix, expected):
    """Verify that ``filter_by_prefix`` returns only strings that start with ``prefix``."""
    result = filter_by_prefix(strings, prefix)
    assert result == expected

# 2. Order preservation â the returned list should keep original order

def test_filter_by_prefix_order_preserve():
    strings = ["dog", "cat", "bird", "doe", "camel"]
    result = filter_by_prefix(strings, "c")
    assert result == ["cat", "camel"]

# 3. Empty prefix â should match every string

def test_filter_by_prefix_empty_prefix_returns_all():
    strings = ["x", "xy", "xyz"]
    result = filter_by_prefix(strings, "")
    assert result == strings

# 4. Prefix longer than some strings â those strings should be omitted

def test_filter_by_prefix_longer_than_some_strings():
    strings = ["a", "ab", "abc", "abcd"]
    result = filter_by_prefix(strings, "abcde")
    assert result == []

# 5. No mutation of the input list â original list unchanged after the call

def test_filter_by_prefix_does_not_mutate_input():
    strings = ["alpha", "beta", "gamma"]
    original = strings.copy()
    _ = filter_by_prefix(strings, "b")
    assert strings == original  # Input list must remain unchanged

# 6. Check that the function returns a new list (not the same object)

def test_filter_by_prefix_returns_new_list():
    strings = ["foo", "bar"]
    result = filter_by_prefix(strings, "f")
    assert result is not strings
}
"""


def filter_by_prefix(strings: List[str], prefix: str) -> List[str]:
    """Filter an input list of strings only for ones that start with a given prefix.

    Parameters
    ----------
    strings : List[str]
        The list of strings to filter.
    prefix : str
        The prefix to check against each string.

    Returns
    -------
    List[str]
        A new list containing only those strings that begin with `prefix`, in the
        same order as they appeared in ``strings``.

    Examples
    --------
    >>> filter_by_prefix([], 'a')
    []
    >>> filter_by_prefix(['abc', 'bcd', 'cde', 'array'], 'a')
    ['abc', 'array']
    """
    # str.startswith handles all edge cases: empty prefix matches all, longer
    # prefixes return False, order is preserved, and the result is a fresh list.
    return [s for s in strings if s.startswith(prefix)]



METADATA = {
    'author': 'jt',
    'dataset': 'test'
}


def test_check():
    assert filter_by_prefix([], 'john') == []
    assert filter_by_prefix(['xxx', 'asd', 'xxy', 'john doe', 'xxxAAA', 'xxx'], 'xxx') == ['xxx', 'xxxAAA', 'xxx']

