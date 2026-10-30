def test_int_to_mini_roman_basic_cases():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(39) == 'xxxix'
    assert int_to_mini_roman(58) == 'lviii'
    assert int_to_mini_roman(199) == 'cxcix'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(991) == 'cmxcxi'

def test_int_to_mini_roman_upper_bounds():
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_returns_str():
    assert isinstance(int_to_mini_roman(42), str)

