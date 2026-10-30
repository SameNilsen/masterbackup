def test_cycpattern_substring_true():
    assert cycpattern_check("hello", "ell") is True

def test_cycpattern_substring_false():
    assert cycpattern_check("abcd", "abd") is False

def test_cycpattern_rotation_true():
    assert cycpattern_check("abab", "baa") is True

def test_cycpattern_rotation_false():
    assert cycpattern_check("whassup", "psus") is False

def test_cycpattern_longer_b_false():
    assert cycpattern_check("abc", "abcd") is False

def test_cycpattern_empty_strings_true():
    assert cycpattern_check("", "") is True

def test_cycpattern_empty_a_false():
    assert cycpattern_check("", "a") is False

def test_cycpattern_b_equals_a_true():
    assert cycpattern_check("abc", "abc") is True

def test_cycpattern_repeating_pattern_true():
    assert cycpattern_check("aaaab", "baaa") is True

def test_cycpattern_non_alpha_false():
    assert cycpattern_check("efef", "eeff") is False

def test_cycpattern_case_sensitive():
    assert cycpattern_check("Hello", "ell") is False

def test_cycpattern_sim_en_true():
    assert cycpattern_check("himenss", "simen") is True

