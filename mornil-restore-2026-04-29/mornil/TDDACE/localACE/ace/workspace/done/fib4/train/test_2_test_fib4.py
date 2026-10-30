def test_fib4_base_cases():
    """Check the defined base values of the sequence."""
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_docstring_examples():
    """Examples given in the function docstring.
    These are small checks that confirm the recurrence is applied correctly.
    """
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14


def _expected_fib4(n: int) -> int:
    """Return the n-th Fib4 number using an explicit loop.
    This helper mimics the recurrence and is used to compute expected values
    for arbitrary indices during tests.
    """
    seq = [0, 0, 2, 0]
    if n < 4:
        return seq[n]
    for i in range(4, n + 1):
        seq.append(seq[-1] + seq[-2] + seq[-3] + seq[-4])
    return seq[n]


def test_fib4_arbitrary_indices():
    """Verify correctness for a selection of larger indices."""
    indices = [8, 9, 10, 12, 15, 18, 25]
    for idx in indices:
        expected = _expected_fib4(idx)
        assert fib4(idx) == expected, f"Expected fib4({idx}) == {expected}"


def test_fib4_type_and_value_validation():
    """Ensure proper exceptions are raised for invalid input types and values."""
    # Nonâinteger input should raise TypeError
    try:
        fib4(3.7)
        assert False, "fib4 did not raise TypeError for float input"
    except TypeError:
        pass

    try:
        fib4("4")
        assert False, "fib4 did not raise TypeError for string input"
    except TypeError:
        pass

    # Negative integers should raise ValueError
    try:
        fib4(-1)
        assert False, "fib4 did not raise ValueError for negative input"
    except ValueError:
        pass

def fib4(n: int) -> int:
    """Return the n-th element of the fib4 sequence.

    Sequence definition:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)      (n >= 4)

    Parameters
    ----------
    n : int
        Nonânegative index to compute; must be an integer.

    Returns
    -------
    int
        The nâth fib4 value.

    Raises
    ------
    TypeError
        If ``n`` is not an :class:`int`.
    ValueError
        If ``n`` is negative.
    """

    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be nonânegative")

    # Base values
    if n < 4:
        base = [0, 0, 2, 0]
        return base[n]

    # Use a sliding window for efficient calculation
    a, b, c, d = 0, 0, 2, 0
    for _ in range(4, n + 1):
        a, b, c, d = b, c, d, a + b + c + d
    return d



METADATA = {}


def test_check():
    assert fib4(5) == 4
    assert fib4(8) == 28
    assert fib4(10) == 104
    assert fib4(12) == 386





