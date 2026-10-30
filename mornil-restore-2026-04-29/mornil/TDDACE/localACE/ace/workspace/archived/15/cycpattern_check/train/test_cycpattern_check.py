import pytest

@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Examples from the docstring
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
        # Rotation vs reversal
        ("abc", "cba", False),  # reversed but not a rotation
        # Valid rotations
        ("abc", "bca", True),
        ("abc", "cab", True),
        # Identical strings
        ("abcd", "abcd", True),
        # Longer "b"
        ("abcd", "abcdabc", False),
        # Empty strings
        ("", "", True),
        ("abc", "", True),
        ("", "abc", False),
        # Repeating patterns
        ("abcabc", "cab", True),
        ("aaaa", "aa", True),
        ("aaaa", "aaa", True),
        # Very short strings
        ("ab", "ba", True),
        # "b" longer than "a"
        ("abc", "abcde", False),
    ],
)
def test_cycpattern_check(a, b, expected):
    assert cycpattern_check(a, b) == expected


def cycpattern_check(a: str, b: str) -> bool:
    """
    Returns True if any rotation of the string `b` is a substring of string `a`.

    Rotations are obtained by moving leading characters of `b` to the end
    in their original order. For example, ``b = "abc"`` has rotations
    ``"abc"`` (original), ``"bca"`` (shift left by 1), and ``"cab"`` (shift
    left by 2).

    Empty string handling:
        - An empty ``b`` matches every string (the empty substring is
          always present).
        - If ``b`` is longer than ``a``, no rotation can appear, so return
          ``False``.

    Parameters:
    ----------
    a : str
        Candidate string to search within.
    b : str
        Pattern string whose rotations are to be checked.

    Returns:
    -------
    bool
        ``True`` if any rotation of ``b`` occurs in ``a``, else ``False``.
    """
    if not b:
        return True
    if len(b) > len(a):
        return False
    doubled = b + b
    n = len(b)
    for i in range(n):
        rotation = doubled[i:i + n]
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

