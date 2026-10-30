def test_flip_returns_same_when_no_letters():
    assert flip_case("12345!@#$") == "12345!@#$"


def test_flip_empty_string():
    assert flip_case("") == ""


def test_flip_all_uppercase():
    assert flip_case("ABC") == "abc"


def test_flip_all_lowercase():
    assert flip_case("xyz") == "XYZ"


def test_flip_mixed_case():
    assert flip_case("Hello World") == "hELLO wORLD"


def test_flip_unicode_characters():
    # Test with German umlauts as an example of nonâASCII alphabetic characters
    assert flip_case("ÃÃÃ") == "Ã¤Ã¶Ã¼"
    assert flip_case("Ã¤Ã¶Ã¼") == "ÃÃÃ"


def test_double_flip_returns_original():
    s = "Case Mix 123"
    assert flip_case(flip_case(s)) == s


def test_return_type_is_string():
    result = flip_case("Test")
    assert isinstance(result, str)
    assert result is not None


