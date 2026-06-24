class Greetings:
    def __init__(self, name):
        self.name = name

    def hello(self):
        print(f"Hello, {self.name} ~~!")

    def new_friend(self, name):
        print(f"nice to meet you, {name} ~~!")


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def sleep(self):
        print(f"{self.name} is sleeping.")

    def eat(self):
        print(f"{self.name} is eating.")


class Dog(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def bark(self):
        print("bark bark bark~~!")


class Cat(Animal):
    def __init__(self, name, age):
        super().__init__(name, age)

    def meow(self):
        print("meow meow meow~~!")
