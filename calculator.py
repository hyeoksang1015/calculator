def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def divide(x, y):
    if y == 0:
        raise ValueError("Cannot divide by zero.")
    return x / y
