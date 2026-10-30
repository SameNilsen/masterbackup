import pytest


def test_right_angle_triangle_basic():
    assert right_angle_triangle(3, 4, 5) is True


def test_right_angle_triangle_permutation():
    assert right_angle_triangle(5, 3, 4) is True


def test_right_angle_triangle_nonright_valid():
    assert right_angle_triangle(2, 3, 4) is False


def test_right_angle_triangle_not_a_triangle():
    assert right_angle_triangle(1, 1, 3) is False


def test_right_angle_triangle_negative_sides():
    assert right_angle_triangle(-3, 4, 5) is False


def test_right_angle_triangle_zero_sides():
    assert right_angle_triangle(0, 3, 4) is False


def test_right_angle_triangle_float_precision():
    assert right_angle_triangle(0.6, 0.8, 1.0) is True


@pytest.mark.parametrize('a,b,c', [
    (3, 4, 5),
    (5, 12, 13),
    (6, 8, 10),
    (7, 24, 25),
    (300, 400, 500),
])

def test_right_angle_triangle_many(a, b, c):
    assert right_angle_triangle(a, b, c) is True


def test_right_angle_triangle_return_type():
    assert isinstance(right_angle_triangle(3, 4, 5), bool)


def right_angle_triangle(a, b, c):
    """Return True if (a, b, c) can be the sides of a rightâangled triangle.

    The function accepts integers or floats.  It returns ``False`` for
    nonâpositive sides, configurations that do not satisfy the triangle
    inequality, or if the Pythagorean relation does not hold within a tiny
    tolerance.  ``math.isclose`` is used so that floatingâpoint values such
    as ``0.6, 0.8, 1.0`` are recognised as a right triangle.
    """
    import math

    # Ensure all arguments are numeric and strictly positive
    for side in (a, b, c):
        if not isinstance(side, (int, float)) or side <= 0:
            return False

    # Sort sides so that ``c`` becomes the largest side
    a, b, c = sorted((a, b, c))

    # Triangle inequality â the sum of the two smaller sides must be strictly greater than the largest side
    if a + b <= c:
        return False

    # Pythagorean test using a tolerance for floatingâpoint arithmetic
    return math.isclose(a * a + b * b, c * c, rel_tol=1e-9, abs_tol=1e-9)

def test_check():

    # Check some simple cases
    assert right_angle_triangle(3, 4, 5) == True, "This prints if this assert fails 1 (good for debugging!)"
    assert right_angle_triangle(1, 2, 3) == False
    assert right_angle_triangle(10, 6, 8) == True
    assert right_angle_triangle(2, 2, 2) == False
    assert right_angle_triangle(7, 24, 25) == True
    assert right_angle_triangle(10, 5, 7) == False
    assert right_angle_triangle(5, 12, 13) == True
    assert right_angle_triangle(15, 8, 17) == True
    assert right_angle_triangle(48, 55, 73) == True

    # Check some edge cases that are easy to work out by hand.
    assert right_angle_triangle(1, 1, 1) == False, "This prints if this assert fails 2 (also good for debugging!)"
    assert right_angle_triangle(2, 2, 10) == False

