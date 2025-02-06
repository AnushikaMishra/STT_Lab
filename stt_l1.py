"""
factorial.py - A simple script to compute the factorial of a number.

This script prompts the user for a number and calculates its factorial using recursion.
"""

def factorial(n):
    """
    Recursively calculates the factorial of a given number.

    Args:
        n (int): The number to compute the factorial for.

    Returns:
        int: The factorial of the number.
    """
    if n in (0, 1):  # ✅ Fix: Simplified condition
        return 1
    return n * factorial(n - 1)

def main():
    """Main function to get user input and print the factorial."""
    try:
        num = int(input("Enter a number: "))
        if num < 0:
            print("Factorial is not defined for negative numbers.")
        else:
            print(f"The factorial of {num} is {factorial(num)}")
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
