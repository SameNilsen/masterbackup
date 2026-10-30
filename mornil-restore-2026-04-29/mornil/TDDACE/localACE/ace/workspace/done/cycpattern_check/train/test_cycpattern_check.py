import pytest

# Helper that mirrors the logic behind ``cycpattern_check`` for test verification

def expected_cycpattern(s1: str, s2: str) -> bool:
    # An empty second string is always considered a substring.
    if s2 == "":
        return True
    n = len(s2)
    for i in range(n):
        rot = s2[i:] + s2[:i]  # generate rotation
        if rot in s1:
            return True
    return False

# Parametrised test covering all key scenarios
@pytest.mark.parametrize(
    "s1, s2",
    [
        ("hello", "ell"),          # simple substring
        ("abcd", "abd"),           # no match
        ("whassup", "psus"),      # rotation does not match
        ("abab", "baa"),           # rotation matches
        ("efef", "eeff"),          # rotation does not match
        ("himenss", "simen"),      # rotation matches
        ("Hello", "ell"),          # case sensitive mismatch
        ("abc", ""),               # empty second string
        ("", "abc"),               # empty first string
        ("", ""),                  # both empty
        ("a", "a"),                # single character match
        ("aaa", "aa"),             # repeated characters
        ("abcde", "cdeab"),        # rotation aligns with full string
    ],
)
def test_cycpattern_check(s1, s2):
    """Ensure ``cycpattern_check`` behaves as expected for a variety of cases."""
    expected = expected_cycpattern(s1, s2)
    assert cycpattern_check(s1, s2) == expected

def cycpattern_check(a: str, b: str) -> bool:
    """Return True if *any* rotation of *b* is a substring of *a*.

    An empty *b* is always considered a substring.  The function raises a
    ``TypeError`` if either argument is not a string.  The algorithm
    iterates over all rotations of *b* and checks each against *a*.
    """

    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both arguments must be strings")

    # An empty second string always matches.
    if b == "":
        return True

    n = len(b)
    for i in range(n):
        rot = b[i:] + b[:i]
        if rot in a:
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





