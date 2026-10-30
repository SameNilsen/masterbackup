def test_cycpattern_check_examples():
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("hello", "ell") is True
    assert cycpattern_check("whassup", "psus") is False
    assert cycpattern_check("abab", "baa") is True
    assert cycpattern_check("efef", "eeff") is False
    assert cycpattern_check("himenss", "simen") is True

def test_cycpattern_check_edge_cases():
    # Empty pattern
    assert cycpattern_check("abcd", "") is True
    assert cycpattern_check("", "") is True
    # Pattern longer than target
    assert cycpattern_check("abc", "abcd") is False
    # Exact matches and rotations
    assert cycpattern_check("abc", "abc") is True
    assert cycpattern_check("abcde", "cdeab") is True
    assert cycpattern_check("abcde", "bcdea") is True
    # No matching rotation
    assert cycpattern_check("abcde", "cdeca") is False

def test_cycpattern_check_no_side_effects():
    a = "abcd"
    b = "bc"
    a_copy = a
    b_copy = b
    cycpattern_check(a, b)
    assert a == a_copy and b == b_copy

def test_cycpattern_check_case_sensitivity():
    assert cycpattern_check("AbC", "aB") is False
    assert cycpattern_check("AbC", "bC") is False
    assert cycpattern_check("abc", "ABC") is False

# Additional tests for rotations with duplicate characters

def test_cycpattern_check_duplicates():
    assert cycpattern_check("aaa", "aa") is True
    assert cycpattern_check("abab", "baba") is True
    assert cycpattern_check("abcabc", "cabcab") is True
    assert cycpattern_check("abcabc", "cabbac") is False

def cycpattern_check(a: str, b: str) -> bool:
    """Return ``True`` if any rotation of ``b`` is a substring of ``a``.

    Parameters
    ----------
    a : str
        The target text.
    b : str
        The pattern whose rotations are to be searched.

    Returns
    -------
    bool
        ``True`` if any rotation of ``b`` appears in ``a``, else ``False``.

    Notes
    -----
    * If ``b`` is empty, it is considered a substring of any ``a``.
    * If ``b`` is longer than ``a``, the function immediately returns ``False``.
    * The function is case-sensitive and does not modify its arguments.
    """
    if not b:
        return True
    if len(b) > len(a):
        return False
    # Check each rotation of b
    for i in range(len(b)):
        if b[i:] + b[:i] in a:
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

