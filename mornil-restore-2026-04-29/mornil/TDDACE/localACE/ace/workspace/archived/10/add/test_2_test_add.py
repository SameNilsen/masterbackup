import pytest


def test_add_positive_numbers():
    assert add(2, 3) == 5
    assert add(5, 7) == 12


def test_add_zero():
    assert add(0, 5) == 5
    assert add(5, 0) == 5
    assert add(0, 0) == 0


def test_add_negative_numbers():
    assert add(-2, -3) == -5
    assert add(-5, 7) == 2
    assert add(5, -7) == -2


def test_add_large_integers():
    large = 10**100
    assert add(large, large) == 2 * large
    assert add(large, -large) == 0


def test_add_type_error():
    with pytest.raises(TypeError):
        add("2", 3)
    with pytest.raises(TypeError):
        add(2, None)


No final answer found



METADATA = {}


def test_check():
    import random

    assert add(0, 1) == 1
    assert add(1, 0) == 1
    assert add(2, 3) == 5
    assert add(5, 7) == 12
    assert add(7, 5) == 12

    for i in range(100):
        x, y = random.randint(0, 1000), random.randint(0, 1000)
        assert add(x, y) == x + y

