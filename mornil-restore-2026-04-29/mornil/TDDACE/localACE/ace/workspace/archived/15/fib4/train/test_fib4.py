def fib4(n: int):
    '''Computes the n-th element of the Fib4 sequence.

    The sequence is defined as:
    fib4(0) = 0
    fib4(1) = 0
    fib4(2) = 2
    fib4(3) = 0
    fib4(n) = fib4(n-1) + fib4(n-2) + fib4(n-3) + fib4(n-4) for n >= 4.

    Args:
        n: Nonânegative integer index.

    Returns:
        int: The n-th Fib4 number.

    Raises:
        ValueError: If n is negative.
    '''
    if n < 0:
        raise ValueError("n must be non-negative")
    if n == 0:
        return 0
    if n == 1:
        return 0
    if n == 2:
        return 2
    if n == 3:
        return 0
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

