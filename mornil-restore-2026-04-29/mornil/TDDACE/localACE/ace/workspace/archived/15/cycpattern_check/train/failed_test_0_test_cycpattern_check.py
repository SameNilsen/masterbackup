import pytest

# Basic, handâcrafted examples from the specification
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("abcd", "abd", False),
        ("hello", "ell", True),
        ("whassup", "psus", False),
        ("abab", "baa", True),
        ("efef", "eeff", False),
        ("himenss", "simen", True),
    ],
)
def test_cycpattern_basic(a, b, expected):
    assert cycpattern_check(a, b) == expected

# Edgeâcase scenarios
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("short", "longerstring", False),  # b longer than a
        ("abc", "abc", True),              # exact match
        ("xyzxyz", "zyx", False),          # rotation not present
        ("aaa", "", True),                # empty b should match (empty substring)
        ("", "a", False),                 # a empty, b nonâempty
        ("", "", True),                   # both empty
    ],
)
def test_cycpattern_edge_cases(a, b, expected):
    assert cycpattern_check(a, b) == expected

# Rotationâspecific tests, ensuring rotations are correctly examined
@pytest.mark.parametrize(
    "a, b, expected",
    [
        ("baaa", "aaa", True),            # rotation of b="aaa" is still "aaa"
        ("cdefg", "ecd", False),          # no rotation of "ecd" is in a
        ("banana", "anan", True),         # "anan" is rotation of "anan"
        ("abcdabcd", "dabc", True),      # rotation "dabc" appears
        ("aabbcc", "bca", False),         # rotation "abc", "bca", "cab" none in a
    ],
)
def test_cycpattern_rotation_examples(a, b, expected):
    assert cycpattern_check(a, b) == expected

