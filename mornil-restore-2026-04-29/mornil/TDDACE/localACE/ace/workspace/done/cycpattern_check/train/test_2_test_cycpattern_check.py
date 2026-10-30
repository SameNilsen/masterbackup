import pytest

# Helper that reflects the intended logic of cycpattern_check
# Used in tests to validate expected outcomes programmatically

def expected_cycle_check(a: str, b: str) -> bool:
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both arguments must be strings")
    if len(b) == 0:
        return True  # empty string is a substring of any string
    rotations = [b[i:] + b[:i] for i in range(len(b))]
    return any(rot in a for rot in rotations)

# ---------------------------------------------------------------------------
# Concrete test functions
# ---------------------------------------------------------------------------

def test_spec_examples():
    """All examples from the problem statement."""
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("hello", "ell") is True
    assert cycpattern_check("whassup", "psus") is False
    assert cycpattern_check("abab", "baa") is True
    assert cycpattern_check("efef", "eeff") is False
    assert cycpattern_check("himenss", "simen") is True

    # Verify using the helper implementation
    assert expected_cycle_check("abcd", "abd") is False
    assert expected_cycle_check("hello", "ell") is True
    assert expected_cycle_check("whassup", "psus") is False
    assert expected_cycle_check("abab", "baa") is True
    assert expected_cycle_check("efef", "eeff") is False
    assert expected_cycle_check("himenss", "simen") is True


def test_exact_substring_and_rotation_present():
    assert cycpattern_check("hello", "ell") is True
    assert expected_cycle_check("hello", "ell") is True

    assert cycpattern_check("abab", "baa") is True
    assert expected_cycle_check("abab", "baa") is True


def test_rotation_present_multiple():
    # b rotations: "cab", "abc", "bca"
    assert cycpattern_check("abcabc", "cab") is True
    assert expected_cycle_check("abcabc", "cab") is True


def test_no_match():
    assert cycpattern_check("abcde", "abc") is True  # because "abc" is a substring
    assert cycpattern_check("abcdef", "defg") is False
    assert expected_cycle_check("abcdef", "defg") is False


def test_empty_substring():
    # empty b should always match
    assert cycpattern_check("abc", "") is True
    assert expected_cycle_check("abc", "") is True


def test_empty_a_nonempty_b():
    assert cycpattern_check("", "a") is False
    assert expected_cycle_check("", "a") is False


def test_b_longer_than_a():
    assert cycpattern_check("ab", "abc") is False
    assert expected_cycle_check("ab", "abc") is False


def test_return_type_is_bool():
    assert isinstance(cycpattern_check("hello", "ell"), bool)


def test_type_validation_raises_type_error():
    """cycpattern_check should raise TypeError if arguments are not strings."""
    with pytest.raises(TypeError):
        cycpattern_check(123, "a")
    with pytest.raises(TypeError):
        cycpattern_check("abc", 456)
    with pytest.raises(TypeError):
        cycpattern_check([], {})

def cycpattern_check(a, b):
    """Return True if any rotation of ``b`` is a substring of ``a``,
    otherwise False.

    Parameters
    ----------
    a : str
        The string to search inside.
    b : str
        The string whose rotations we want to test.

    Raises
    ------
    TypeError
        If either ``a`` or ``b`` is not a string.

    Notes
    -----
    An empty ``b`` is considered a substring of any string, according
    to the specification.
    """
    # Type validation
    if not isinstance(a, str) or not isinstance(b, str):
        raise TypeError("Both arguments must be strings")

    # Empty ``b`` is always a match
    if len(b) == 0:
        return True

    # Check each rotation of ``b``
    n = len(b)
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





