def right_angle_triangle(a, b, c):
    """
    Returns True if the three sides form a rightâangled triangle, False otherwise.
    """
    # Sort to identify the largest (hypotenuse)
    sides = sorted((a, b, c))
    # Apply the Pythagorean theorem
    return sides[0]**2 + sides[1]**2 == sides[2]**2

def right_angle_triangle(a, b, c):
    """Return True if `a`, `b`, and `c` form a rightâangled triangle.

    Parameters
    ----------
    a, b, c : int or float
        Lengths of the triangle's sides.

    Returns
    -------
    bool
        True if the sides satisfy the Pythagorean theorem and
        correspond to a valid triangle, False otherwise.
    """
    # Ensure that all sides are numbers
    for side in (a, b, c):
        if not isinstance(side, (int, float)):
            raise TypeError("All side lengths must be numeric")

    # All sides must be positive â a triangle cannot have nonâpositive lengths
    if a <= 0 or b <= 0 or c <= 0:
        return False

    # Sort to identify the potential hypotenuse
    x, y, z = sorted((a, b, c))

    # For integer sides we compare exactly; for floats use a tolerance
    if isinstance(x, float) or isinstance(y, float) or isinstance(z, float):
        return abs(x**2 + y**2 - z**2) < 1e-9
    return x**2 + y**2 == z**2

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

