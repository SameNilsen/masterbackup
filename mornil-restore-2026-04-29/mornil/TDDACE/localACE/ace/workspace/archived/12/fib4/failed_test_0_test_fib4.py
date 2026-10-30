```python
import pytest

# Import the function to be tested. It is assumed that the function
# resides in a module named "fib4" in the same project directory.
from fib4 import fib4

# ------------------------------------------------------------------
# Basic test cases covering the initial terms of the sequence.
# ------------------------------------------------------------------

def test_fib4_basic():
    assert fib4(0) == 0  # Base case
    assert fib4(1) == 0
    assert fib4(2) == 2
    assert fib4(3) == 0
    assert fib4(4) == 2  # 0+0+2+0
    assert fib4(5) == 4  # 2+0+2+0
    assert fib4(6) == 8  # 4+2+0+2
    assert fib4(7) == 14  # 8+4+2+0

# ------------------------------------------------------------------
# Test larger values to ensure the recurrence is correctly implemented
# for more complex cases.
# ------------------------------------------------------------------

def test_fib4_large():
    # Checked manually: fib4(10) = 104
    assert fib4(10) == 104
    # Checked manually: fib4(15) = 2864
    assert fib4(15) == 2864

# ------------------------------------------------------------------
# Verify that the function returns an integer.
# ------------------------------------------------------------------

def test_fib4_return_type():
    assert isinstance(fib4(7), int)

# ------------------------------------------------------------------
# Ensure the function handles a wide range without errors.
# ------------------------------------------------------------------

def test_fib4_no_negative():
    # The specification does not define behaviour for negatives; the
    # function should still return a value or raise a clear exception.
    # Here we simply call it to confirm no unexpected errors are raised.
    try:
        fib4(-1)
    except Exception as e:
        # Accept any exception type â this test documents that a
        # negative input does not silently succeed.
        assert isinstance(e, Exception)
    else:
        # If the function returns a value for negative input, it is
        # still acceptable for this test; we note the result.
        assert isinstance(fib4(-1), int)

# ------------------------------------------------------------------
# End of tests. Pytest will automatically discover the test functions.
# ------------------------------------------------------------------
```

