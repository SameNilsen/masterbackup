def test_example_cases():
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True


def test_empty_strings():
    # Empty second string should be considered a substring of any string
    assert cycpattern_check("anystring", "") == True
    # Both strings empty: still True
    assert cycpattern_check("", "") == True
    # Empty first string with nonâempty second string: should be False
    assert cycpattern_check("", "a") == False


def test_first_shorter_than_second():
    assert cycpattern_check("abc", "abcd") == False


def test_case_sensitivity():
    assert cycpattern_check("Hello", "ELL") == False
    assert cycpattern_check("HELLO", "ell") == False
    assert cycpattern_check("hello", "Ell") == False


def test_rotation_matches():
    # Rotation "dabc" of "abcd" appears in "abcdabcd"
    assert cycpattern_check("abcdabcd", "dabc") == True
    # Rotation "bca" of "cab" appears in "acb"
    assert cycpattern_check("acb", "cab") == True


def test_non_alpha_characters():
    assert cycpattern_check("a_b-c.d", "b-c") == True
    assert cycpattern_check("12345", "345") == True
    assert cycpattern_check("12345", "3451") == False


def test_duplicates_and_overlap():
    # b with repeated characters â all rotations identical
    assert cycpattern_check("aaaa", "aa") == True
    # overlapping substring
    assert cycpattern_check("abcabca", "bca") == True


