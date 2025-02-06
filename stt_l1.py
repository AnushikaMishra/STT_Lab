def greet(name):
    """Function to greet a person"""
    return f"Hello, {name}!"

class Person:
    """A class representing a person"""
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display(self):
        """Prints person details"""
        print(f"Name: {self.name}, Age: {self.age}")

if __name__ == "__main__":
    p = Person("Alice", 25)
    p.display()
    print(greet("Alice"))
