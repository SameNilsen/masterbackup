def test_right_angle_triangle_basic():
    assert right_angle_triangle(3, 4, 5)


def test_right_angle_triangle_non_right():
    assert not right_angle_triangle(2, 3, 4)


def test_right_angle_triangle_permuted_legs():
    assert right_angle_triangle(5, 3, 4)


def test_right_angle_triangle_zero_length():
    assert not right_angle_triangle(0, 5, 5)


def test_right_angle_triangle_negative_length():
    assert not right_angle_triangle(-3, 4, 5)


def test_right_angle_triangle_float_sides():
    assert right_angle_triangle(1.5, 2.0, 2.5)


def test_right_angle_triangle_not_a_triangle():
    assert not right_angle_triangle(1, 1, 3)


def test_right_angle_triangle_large_numbers():
    assert right_angle_triangle(3000000, 4000000, 5000000)

def right_angle_triangle(a, b, c):
    """Return True if the lengths a, b, c form a rightâangled triangle.

    The function accepts integers or floats.  All sides must be
    strictly positive and satisfy the triangle inequality.  The
    Pythagorean theorem is checked exactly for integer inputs and
    with a tolerance for floatingâpoint inputs.
    """
    import math

    # Ensure all inputs are numbers and are positive
    for x in (a, b, c):
        if not isinstance(x, (int, float)):
            return False
        if x <= 0:
            return False

    # Sort so that the largest side is candidate for hypotenuse
    a, b, c = sorted([a, b, c])

    # Triangle inequality â must be strict for a nonâdegenerate triangle
    if a + b <= c:
        return False

    lhs = a * a + b * b
    rhs = c * c

    # If all inputs are integers, compare exactly
    if all(isinstance(x, int) for x in (a, b, c)):
        return lhs == rhs

    # Otherwise use an approximate comparison for floats
    return math.isclose(lhs, rhs, rel_tol=1e-9)


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

