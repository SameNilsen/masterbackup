def test_basic_examples():
    assert not cycpattern_check("abcd", "abd")
    assert cycpattern_check("hello", "ell")
    assert not cycpattern_check("whassup", "psus")
    assert cycpattern_check("abab", "baa")
    assert not cycpattern_check("efef", "eeff")
    assert cycpattern_check("himenss", "simen")


def test_edge_cases():
    assert not cycpattern_check("any", "")  # empty second not considered a rotation
    assert not cycpattern_check("short", "longer")  # second longer than first


def test_case_sensitivity():
    assert cycpattern_check("Abcdef", "bcd")  # case sensitive match
    assert not cycpattern_check("Abcdef", "BCD")  # mismatched case


def test_exact_and_repetition():
    assert cycpattern_check("abcd", "abcd")  # identical strings
    assert cycpattern_check("aaaaaa", "aaa")  # repeated characters


def test_single_character_and_not_found():
    assert cycpattern_check("abc", "a")
    assert not cycpattern_check("abc", "z")


def test_rotation_wrap_and_substring():
    assert cycpattern_check("abcd", "cdab")  # rotation equals entire first string
    assert cycpattern_check("abcdabcd", "cdab")  # rotation appears in the middle
    assert cycpattern_check("abcabcabc", "bca")  # rotation appears
    assert not cycpattern_check("abcabc", "cba")  # not a rotation

def cycpattern_check(a: str, b: str) -> bool:
    """Return True if any rotation of ``b`` appears as a substring of ``a``.

    The function performs the following steps:
    1. If ``b`` is empty or longer than ``a``, return False.
    2. Double ``b`` to capture all possible rotations.
    3. For each rotation of length ``len(b)``, check whether it is a substring of ``a``.
    4. Return True if any rotation matches; otherwise return False.
    """
    m, n = len(b), len(a)
    if m == 0 or m > n:
        return False
    double = b + b
    for i in range(m):
        rotation = double[i:i + m]
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

