from calculator import add, subtract

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtraction():
    assert subtract(10, 5) == 5

from calculator import add, subtract, multiply # Update import

def test_multiplication():
    assert multiply(3, 5) == 15
    assert multiply(-1, 5) == -5

import pytest
from calculator import add, subtract, multiply, divide

# ... (previous tests for add, subtract, multiply)

def test_division():
    assert divide(10, 2) == 5
    assert divide(9, 3) == 3
    assert divide(5, 2) == 2.5

def test_divide_by_zero():
    with pytest.raises(ValueError, match="Cannot divide by zero!"):
        divide(10, 0)