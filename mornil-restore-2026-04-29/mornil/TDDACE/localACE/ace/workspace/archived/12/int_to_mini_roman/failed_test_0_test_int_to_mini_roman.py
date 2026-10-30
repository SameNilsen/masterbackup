def test_int_to_mini_roman_basic():
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(4) == 'iv'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(9) == 'ix'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(90) == 'xc'

def test_int_to_mini_roman_edge_cases():
    assert int_to_mini_roman(40) == 'xl'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(900) == 'cm'
    assert int_to_mini_roman(1000) == 'm'

def test_int_to_mini_roman_examples():
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'

def test_int_to_mini_roman_random_and_limits():
    assert int_to_mini_roman(555) == 'dlv'
    assert int_to_mini_roman(999) == 'cmxcix'
    assert int_to_mini_roman(991) == 'cmxcxi'

def test_int_to_mini_roman_lowercase():
    for num in [1, 4, 19, 152, 426, 555, 999, 1000]:
        result = int_to_mini_roman(num)
        assert result.islower(), f'Roman numeral not lowercase for {num}: {result}'

