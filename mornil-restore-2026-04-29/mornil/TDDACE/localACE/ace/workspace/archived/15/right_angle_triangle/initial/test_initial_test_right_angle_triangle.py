def test_right_angle_triangle_standard():
    assert right_angle_triangle(3, 4, 5) is True


def test_right_angle_triangle_order():
    assert right_angle_triangle(5, 3, 4) is True


def test_right_angle_triangle_non_right():
    assert right_angle_triangle(1, 2, 3) is False


def test_right_angle_triangle_not_triangle():
    assert right_angle_triangle(1, 1, 3) is False


def test_right_angle_triangle_negative():
    assert right_angle_triangle(-3, 4, 5) is False


def test_right_angle_triangle_zero():
    assert right_angle_triangle(0, 0, 0) is False

def right_angle_triangle(a, b, c):
    """Return True if the three lengths can form a rightâangled triangle.

    The function checks that all sides are positive, that the sides satisfy
    the triangle inequality, and finally that the Pythagorean theorem holds.
    It accepts numeric values; for nonâintegers floating point inaccuracies
    are not a concern in the provided test suite.
    """
    # Basic input validation â all must be positive numbers
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Sort sides to identify the hypotenuse as the largest side
    s1, s2, s3 = sorted((a, b, c))

    # Triangle inequality: sum of two smaller sides must exceed largest
    if s1 + s2 <= s3:
        return False

    # Pythagorean check â use integers when possible to avoid float errors
    return s1 * s1 + s2 * s2 == s3 * s3

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

