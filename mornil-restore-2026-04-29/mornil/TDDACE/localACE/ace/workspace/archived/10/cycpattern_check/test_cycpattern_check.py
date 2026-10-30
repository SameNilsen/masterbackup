def test_cycpattern_check_basic_cases():
    assert cycpattern_check("abcd","abd") is False
    assert cycpattern_check("hello","ell") is True
    assert cycpattern_check("whassup","psus") is False
    assert cycpattern_check("abab","baa") is True
    assert cycpattern_check("efef","eeff") is False
    assert cycpattern_check("himenss","simen") is True


def test_cycpattern_check_substring_and_unequal():
    assert cycpattern_check("abcde","abcde") is True
    assert cycpattern_check("abcde","cdeab") is True


def test_cycpattern_check_rotations_across_boundaries():
    assert cycpattern_check("abcabc","bca") is True
    assert cycpattern_check("abcabc","cab") is True


def test_cycpattern_check_repeated_characters():
    assert cycpattern_check("aaa","a") is True
    assert cycpattern_check("aaaa","aa") is True


def test_cycpattern_check_b_longer_than_a():
    assert cycpattern_check("abc","abcd") is False



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



def cycpattern_check(a: str, b: str) -> bool:
    """Return True if any rotation of b is a substring of a.

    The function works by generating all rotations of *b* and checking
    whether each rotation appears in *a*.  An empty *b* is considered
    a substring of any string, hence the function returns True.
    If *b* is longer than *a*, the check is futile and the function
    returns False immediately.
    """
    if len(b) == 0:
        return True
    if len(b) > len(a):
        return False
    double_b = b + b
    n = len(b)
    for i in range(n):
        rotation = double_b[i:i+n]
        if rotation in a:
            return True
    return False

