def add(a, b):
    return a + b 

def subtract(a, b):
    return a - b
    
def muldiv(a,b):
    return ((a*b)+(a/b))

def divmul(a,b):
    return ((a/b)+(a*b))
    
def multiply(a, b):
    return a * b

def muladd(a, b):
    return ((a*b)+(a+b))

def addmul(a, b):
    return ((a+b)*(a*b))

def divide(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero!")
    return a / b
