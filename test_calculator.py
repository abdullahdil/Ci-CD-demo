from calculator import add, subtract

def test_addition():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0

def test_subtraction():
    assert subtract(10, 5) == 5