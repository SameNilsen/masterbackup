def test_examples_from_docstring():
    assert cycpattern_check("abcd", "abd") is False
    assert cycpattern_check("hello", "ell") is True
    assert cycpattern_check("whassup", "psus") is False
    assert cycpattern_check("abab", "baa") is True
    assert cycpattern_check("efef", "eeff") is False
    assert cycpattern_check("himenss", "simen") is True


def test_rotation_matches():
    # Rotation that appears in the first string
    assert cycpattern_check("abc", "cab") is True  # 'cab' is a rotation of 'abc'
    assert cycpattern_check("cba", "abc") is True  # 'abc' rotated gives 'cba'


def test_non_matching_cases():
    assert cycpattern_check("abc", "abcd") is False  # b longer than a
    assert cycpattern_check("", "a") is False


def test_empty_string_handling():
    # Empty b should always be a substring
    assert cycpattern_check("", "") is True
    assert cycpattern_check("abc", "") is True
    # Empty a with non-empty b is impossible
    assert cycpattern_check("", "a") is False


def test_exact_match_and_casesensitivity():
    assert cycpattern_check("TestString", "TestString") is True
    assert cycpattern_check("TestString", "teststring") is False

