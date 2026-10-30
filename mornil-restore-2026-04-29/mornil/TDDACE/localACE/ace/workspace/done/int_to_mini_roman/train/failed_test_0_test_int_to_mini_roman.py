def test_basic_conversion():
    """Test conversion for the core Roman numerals."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(5) == 'v'
    assert int_to_mini_roman(10) == 'x'
    assert int_to_mini_roman(50) == 'l'
    assert int_to_mini_roman(100) == 'c'
    assert int_to_mini_roman(500) == 'd'
    assert int_to_mini_roman(1000) == 'm'


def test_additive_and_subtractive():
    """Test numbers that involve both additive and subtractive notation."""
    assert int_to_mini_roman(19) == 'xix'
    assert int_to_mini_roman(152) == 'clii'
    assert int_to_mini_roman(426) == 'cdxxvi'
    assert int_to_mini_roman(4)  == 'iv'
    assert int_to_mini_roman(9)  == 'ix'
    assert int_to_mini_roman(14) == 'xiv'
    assert int_to_mini_roman(44) == 'xliv'
    assert int_to_mini_roman(49) == 'xlix'
    assert int_to_mini_roman(94) == 'xciv'
    assert int_to_mini_roman(99) == 'xcix'
    assert int_to_mini_roman(400) == 'cd'
    assert int_to_mini_roman(499) == 'cdxcix'
    assert int_to_mini_roman(999) == 'cmxcix'


def test_boundary_cases():
    """Test the exact minimum and maximum allowed values."""
    assert int_to_mini_roman(1) == 'i'
    assert int_to_mini_roman(1000) == 'm'


def test_type_validation():
    """Confirm function raises TypeError for nonâinteger inputs."""
    with pytest.raises(TypeError):
        int_to_mini_roman('a')
    with pytest.raises(TypeError):
        int_to_mini_roman(5.5)
    with pytest.raises(TypeError):
        int_to_mini_roman([5])


def test_value_range_errors():
    """Confirm function raises ValueError for numbers outside 1â1000."""
    with pytest.raises(ValueError):
        int_to_mini_roman(0)
    with pytest.raises(ValueError):
        int_to_mini_roman(1001)
    with pytest.raises(ValueError):
        int_to_mini_roman(-10)


def test_output_is_lowercase():
    """Ensure the numeral is always returned in lowercase."""
    for n in [1, 4, 9, 19, 152, 426, 999, 1000]:
        assert int_to_mini_roman(n).islower()

