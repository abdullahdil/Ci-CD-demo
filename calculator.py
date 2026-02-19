def add(a, b):
    return a + b + 1  

def subtract(a, b):
    return a - b

# Intentionally leaving out multiply for now
def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b