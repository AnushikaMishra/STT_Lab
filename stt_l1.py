class Person:
    """A class representing a person."""
    
    def __init__(self, name, age):
        """Initializes a new person with name and age."""
        self.name = name
        self.age = age

    def display(self):
        """Displays person details."""
        print(f"Name: {self.name}, Age: {self.age}")

    def is_eligible_to_vote(self):
        """Checks if the person is eligible to vote."""
        return self.age >= 18


class Student(Person):
    """A class representing a student, inheriting from Person."""
    
    def __init__(self, name, age, grade):
        """Initializes a student with name, age, and grade."""
        super().__init__(name, age)
        self.grade = grade

    def display(self):
        """Displays student details."""
        super().display()
        print(f"Grade: {self.grade}")

    def is_passing(self):
        """Checks if the student is passing (grade >= 50)."""
        return self.grade >= 50


def main():
    # Create instances
    alice = Person("Alice", 25)
    bob = Student("Bob", 17, 45)
    charlie = Student("Charlie", 19, 65)

    # Display information
    alice.display()
    print(f"Eligible to vote: {alice.is_eligible_to_vote()}")
    
    bob.display()
    print(f"Passing: {bob.is_passing()}")

    charlie.display()
    print(f"Passing: {charlie.is_passing()}")


if __name__ == "__main__":
    main()
