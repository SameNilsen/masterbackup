def fib4(n: int):
    """Return the n-th element of the fib4 sequence.
    The sequence is defined by:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4)  for n >= 4
    Parameters
    ----------
    n : int
        Nonânegative integer indexing the sequence.
    Returns
    -------
    int
        The nâth fib4 value.
    """
    if not isinstance(n, int):
        raise TypeError("n must be an integer")
    if n < 0:
        raise ValueError("n must be nonânegative")

    # Base values for n = 0..3
    base = [0, 0, 2, 0]
    if n < 4:
        return base[n]

    # Sliding window for the last four values
    a, b, c, d = base  # a = F(n-4), b = F(n-3), c = F(n-2), d = F(n-1)
    for _ in range(4, n + 1):
        e = a + b + c + d
        a, b, c, d = b, c, d, e
    return d



METADATA = {}


def test_check():
    assert fib4(5) == 4
    assert fib4(8) == 28
    assert fib4(10) == 104
    assert fib4(12) == 386





