def test_add_positive_numbers():
    assert add(2, 3) == 5


def test_add_negative_numbers():
    assert add(-5, -7) == -12


def test_add_positive_and_negative():
    assert add(10, -3) == 7


def test_add_zero():
    assert add(0, 0) == 0


def test_add_large_numbers():
    assert add(10**12, 10**12) == 2 * 10**12


def test_return_type():
    assert isinstance(add(1, 2), int)


