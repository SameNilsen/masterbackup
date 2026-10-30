def test_basic_examples():
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("hello", "ell") is True
    assert cycpattern_check("whassup", "psus") is False
    assert cycpattern_check("abab", "baa") is True
    assert cycpattern_check("efef", "eeff") is False
    assert cycpattern_check("himenss", "simen") is True


def test_empty_b():
    assert cycpattern_check("anystring", "") is True


def test_b_longer_than_a():
    assert cycpattern_check("abc", "abcd") is False


def test_reversed_string():
    assert cycpattern_check("abc", "cba") is False


def test_rotation_variants():
    # Direct substring that matches a rotation
    assert cycpattern_check("abcdef", "def") is True
    # Single character rotation
    assert cycpattern_check("abcdef", "f") is True
    # Rotation that spans the wrapâaround in 'b'
    assert cycpattern_check("abcdef", "efa") is True


def test_duplicate_characters():
    assert cycpattern_check("bbbbb", "bbb") is True
    assert cycpattern_check("aaaa", "aa") is True


def test_overlaps_and_multiple_matches():
    assert cycpattern_check("xyzabcde", "cde") is True

def cycpattern_check(a: str, b: str) -> bool:
    """Return True if any rotation of ``b`` is a substring of ``a``.

    Empty ``b`` always matches.  The comparison treats ``a`` as circular
    by checking against ``a + a``.
    """
    if not b:
        return True
    if len(b) > len(a):
        return False

    doubled_a = a + a
    doubled_b = b + b
    for i in range(len(b)):
        rotation = doubled_b[i : i + len(b)]
        if rotation in doubled_a:
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

