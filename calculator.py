def add(a, b):
    return a + b


def multiply(a, b):
    return a * b


def subtract(a, b):
    return a - b


def divide(x, y):
    if y == 0:
        return None
    return x / y


class Greetings:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name} ~~!")

    def new_friend(self, name):
        print(f"nice to meet you, {name} ~~!")
