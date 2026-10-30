def test_flip_case_basic() -> None:
    assert flip_case('Hello') == 'hELLO'


def test_flip_case_empty() -> None:
    assert flip_case('') == ''


def test_flip_case_all_lower() -> None:
    input_str = 'abcde123!$'
    expected = 'ABCDE123!$'
    assert flip_case(input_str) == expected


def test_flip_case_all_upper() -> None:
    input_str = 'ABCDE123!$'
    expected = 'abcde123!$'
    assert flip_case(input_str) == expected


def test_flip_case_mixed_with_numbers() -> None:
    input_str = 'a1B2c3'
    expected = 'A1b2C3'
    assert flip_case(input_str) == expected


def test_flip_case_unicode_letters() -> None:
    # The Unicode codepoint for "Ã±" has a lowerâcase mapping, and "Ã" has an upperâcase mapping.
    input_str = 'Ã±Ã'
    expected = 'ÃÃ¡'
    assert flip_case(input_str) == expected


def test_flip_case_mixed_unicode_and_punctuation() -> None:
    input_str = 'AaBbCcÃ±Ã 1,2,3'
    expected = 'aAbBcCdNÃ 1,2,3'
    # The expected string is calculated by manually applying swapcase to letters only.
    assert flip_case(input_str) == expected


