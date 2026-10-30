import pytest

# Test the given examples
@pytest.mark.parametrize(
    "a,b,expected",
    [
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
    ],
)
def test_cycpattern_check_examples(a, b, expected):
    assert cycpattern_check(a, b) == expected

# Edgeâcase tests
@pytest.mark.parametrize(
    "a,b,expected",
    [
        # Empty strings
        ("", "", False),
        ("", "a", False),
        ("a", "", False),
        # Simple matches
        ("a", "a", True),
        # b longer than a
        ("ab", "abc", False),
        # Repeating characters
        ("aaaa", "aa", True),
        ("ab", "b", True),
        ("ab", "ba", True),
        ("ab", "bb", False),
    ],
)
def test_cycpattern_check_edge_cases(a, b, expected):
    assert cycpattern_check(a, b) == expected


def cycpattern_check(a, b):
    """Return True if any leftârotation of b appears as a substring of a.

    Just iterate over all rotations of b and test them against a.
    """
    n = len(b)
    if n == 0:
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

