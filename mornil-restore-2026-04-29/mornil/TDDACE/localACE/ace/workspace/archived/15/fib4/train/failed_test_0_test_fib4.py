def test_fib4_base_cases():
    assert fib4(0) == 0
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0


def test_fib4_small_values():
    assert fib4(4) == 2
    assert fib4(5) == 4
    assert fib4(6) == 8
    assert fib4(7) == 14


def test_fib4_iterative_correctness():
    def expected(n):
        if n <= 3:
            return [0, 0, 2, 0][n]
        f = [0, 0, 2, 0]
        for i in range(4, n + 1):
            f.append(f[-1] + f[-2] + f[-3] + f[-4])
        return f[-1]
    for n in range(0, 20):
        assert fib4(n) == expected(n)


def test_fib4_negative_input_raises():
    import pytest
    with pytest.raises(Exception):
        fib4(-1)


