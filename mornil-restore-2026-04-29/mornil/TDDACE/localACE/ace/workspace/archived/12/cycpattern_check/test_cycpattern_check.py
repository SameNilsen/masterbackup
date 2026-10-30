import pytest

@pytest.mark.parametrize(
    "first, second, expected",
    [
        # Docstring examples
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
        # Edge cases: length differences
        ("ab", "abc", False),               # second longer than first
        ("abc", "abc", True),               # identical strings
        ("abc", "bca", True),               # rotation
        ("abc", "cab", True),               # rotation
        ("abc", "cba", False),              # not a rotation
        # Rotations across boundaries
        ("abcdabcd", "bcda", True),
        ("abcdabcd", "adbc", False),
        # Repeated patterns
        ("ababab", "bab", True),
        ("abcde", "eab", False),
        ("abcde", "cde", True),
        # Singleâcharacter tests
        ("abc", "a", True),
        ("a", "a", True),
        # Caseâsensitivity
        ("Abc", "bc", True),
        ("Abc", "BC", False),
    ],
)

def test_cycpattern_check(first, second, expected):
    assert cycpattern_check(first, second) == expected


def cycpattern_check(first: str, second: str) -> bool:
    """Return True if any rotation of *second* appears as a substring in *first*.

    Parameters
    ----------
    first: str
        The candidate string that should contain a rotation of ``second``.
    second: str
        The string whose rotations are to be searched.

    Returns
    -------
    bool
        ``True`` if any rotation of ``second`` is found within ``first``;
        otherwise ``False``.
    """
    la, lb = len(first), len(second)
    # Impossible when second is longer or empty
    if lb == 0 or lb > la:
        return False

    doubled = second + second
    for i in range(lb):
        rot = doubled[i : i + lb]
        if rot in first:
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

