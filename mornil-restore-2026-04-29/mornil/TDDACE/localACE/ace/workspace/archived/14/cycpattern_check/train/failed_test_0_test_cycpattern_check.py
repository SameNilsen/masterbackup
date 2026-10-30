def test_cycpattern_check_examples():
    """Verify the six examples from the specification."""
    assert cycpattern_check("abcd", "abd") == False
    assert cycpattern_check("hello", "ell") == True
    assert cycpattern_check("whassup", "psus") == False
    assert cycpattern_check("abab", "baa") == True
    assert cycpattern_check("efef", "eeff") == False
    assert cycpattern_check("himenss", "simen") == True

def test_cycpattern_check_boundary_rotation():
    """Check rotations that match at the beginning or end of ``a``."""
    assert cycpattern_check("baaab", "aab") == True
    assert cycpattern_check("abc", "bca") == False

def test_cycpattern_check_no_match():
    """Ensure function returns False for completely mismatched strings."""
    assert cycpattern_check("abcde", "xyz") == False

def test_cycpattern_check_lengths():
    """Test edge cases when the lengths differ significantly."""
    assert cycpattern_check("abc", "abcd") == False
    assert cycpattern_check("abcd", "abc") == True  # exact substring

def test_cycpattern_check_single_character():
    """Singleâcharacter strings are a basic edge case."""
    assert cycpattern_check("x", "x") == True
    assert cycpattern_check("x", "y") == False

def test_cycpattern_check_unicode():
    """Verify handling of Unicode characters."""
    assert cycpattern_check("cafÃ©", "fÃ©") == True
    assert cycpattern_check("cafÃ©", "fÃ©ca") == False


