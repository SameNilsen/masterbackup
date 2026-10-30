import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
        ("abc", "abc", True),
        ("cba", "abc", False),
        ("abc", "b", True),
        ("abc", "d", False),
        ("abc", "aaaa", False),
        ("aaaaa", "aaab", False),
        ("abcxyz", "cxyzab", True),
        ("a", "a", True),
        ("xyz", "x", True),
        ("xyz", "yzz", False),
    ],
)
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected

def test_cycpattern_check_returns_bool():
    assert isinstance(cycpattern_check("test", "e"), bool)

def cycpattern_check(a: str, b: str) -> bool:
    """Return True if any rotation of *b* is a substring of *a*.

    A rotation of a string *s* is obtained by cutting *s* at some index
    ``i`` and concatenating the two parts in reverse order,
    ``s[i:] + s[:i]``.  For a string of length ``n`` there are ``n``
    such rotations (including the original string when ``i == 0``).

    The function simply iterates over all rotations and checks
    membership in ``a``.  The presence of any matching rotation
    yields ``True``, otherwise ``False``.
    """

    n = len(b)
    if n == 0:
        # An empty rotation cannot match a non-empty string, and the
        # behavior for ``b`` empty is undefined in the tests, so we
        # return ``False``.
        return False

    for i in range(n):
        rotation = b[i:] + b[:i]
        if rotation in a:
            return True
    return False


def test_check():

    # Check some simple cases
    #assert True, "This prints if this assert fails 1 (good for debugging!)"

    # Check some edge cases that are easy to work out by hand.
    #assert True, "This prints if this assert fails 2 (also good for debugging!)"
    assert  cycpattern_check("xyzw","xyw") == False , "test #0"
    assert  cycpattern_check("yello","ell") == True , "test #1"
    assert  cycpattern_check("whattup","ptut") == False , "test #2"
    assert  cycpattern_check("efef","fee") == True , "test #3"
    assert  cycpattern_check("abab","aabb") == False , "test #4"
    assert  cycpattern_check("winemtt","tinem") == True , "test #5"

