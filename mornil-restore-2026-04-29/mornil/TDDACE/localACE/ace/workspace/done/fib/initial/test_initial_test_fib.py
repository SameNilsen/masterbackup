def test_fib_basic_cases():
    assert fib(0) == 0
    assert fib(1) == 1
    assert fib(2) == 1
    assert fib(8) == 21
    assert fib(10) == 55

def test_fib_known_values():
    known_values = [
        (5, 5),
        (20, 6765),
        (30, 832040),
        (50, 12586269025),
        (100, 354224848179261915075)
    ]
    for n, expected in known_values:
        assert fib(n) == expected

def test_fib_negative_input():
    try:
        fib(-1)
    except ValueError:
        pass
    else:
        raise AssertionError("fib(-1) did not raise ValueError")

def test_fib_non_integer_input():
    try:
        fib("10")
    except TypeError:
        pass
    else:
        raise AssertionError("fib('10') did not raise TypeError")

def fib(n: int):
    """Return the *n*âth Fibonacci number.

    The sequence is defined as:
    * fib(0) = 0
    * fib(1) = 1
    * fib(n) = fib(n-1) + fib(n-2) for n >= 2

    Parameters
    ----------
    n : int
        The position in the Fibonacci sequence. Must be a nonânegative integer.

    Returns
    -------
    int
        The *n*âth Fibonacci number.

    Raises
    ------
    TypeError
        If *n* is not an integer.
    ValueError
        If *n* is negative.

    Examples
    --------
    >>> fib(10)
    55
    >>> fib(1)
    1
    >>> fib(8)
    21
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be nonânegative")

    if n == 0:
        return 0
    if n == 1:
        return 1

    a, b = 0, 1
    for _ in range(2, n + 1):
        a, b = b, a + b
    return b



METADATA = {}


def test_check():
    assert fib(10) == 55
    assert fib(1) == 1
    assert fib(8) == 21
    assert fib(11) == 89
    assert fib(12) == 144

