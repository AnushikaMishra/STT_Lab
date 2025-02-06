"""
A sample Python script demonstrating Pylint setup
"""
def add_numbers(a: int, b: int) -> int:
    """
    Adds two numbers and returns the result.
    """
    return a + b


def greet_user(name: str) -> str:
    """
    Returns a greeting message.
    """
    return f"Hello, {name}!"


def main():
    """
    Main function that demonstrates function calls.
    """
    num1, num2 = 5, 10
    print(f"Sum: {add_numbers(num1, num2)}")
    print(greet_user("Anushika"))


if __name__ == "__main__":
    main()
