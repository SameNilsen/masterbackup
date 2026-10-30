def test_cycpattern_check_positive_cases():
    assert cycpattern_check("hello", "ell") is True
    assert cycpattern_check("abab", "baa") is True
    assert cycpattern_check("himenss", "simen") is True
    assert cycpattern_check("abcabc", "bca") is True


def test_cycpattern_check_negative_cases():
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("whassup", "psus") is False
    assert cycpattern_check("efef", "eeff") is False
    assert cycpattern_check("abc", "acb") is False


def test_cycpattern_check_edge_cases():
    assert cycpattern_check("abc", "abc") is True
    assert cycpattern_check("abc", "abcd") is False
    assert cycpattern_check("aaa", "aa") is True
    assert cycpattern_check("Abc", "bC") is False

def cycpattern_check(a: str, b: str) -> bool:
    '''Return True if b or any cyclic rotation of b occurs as a substring in a.

    The function checks whether any rotation of the second string b is a
    substring of the first string a.  The implementation is straightforward:

    1. If b is longer than a it cannot be a substring â return False.
    2. Generate all rotations of b.
    3. Test each rotation against a with the in operator.

    The algorithm runs in O(len(a)*len(b)) time and uses O(len(b)) extra
    memory.
    '''
    if len(b) > len(a):
        return False
    for i in range(len(b)):
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

