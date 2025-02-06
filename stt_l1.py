def fibonacci(n):
    """Generate a Fibonacci sequence up to n terms."""
    a, b = 0, 1
    for _ in range(n):
        print(a, end=" ")
        a, b = b, a + b
    print()

def main():
    """Main function to get user input and print Fibonacci sequence."""
    print("Fibonacci Sequence Generator")
    try:
        n = int(input("Enter the number of terms: "))
        if n <= 0:
            print("Please enter a positive integer.")
        else:
            fibonacci(n)
    except ValueError:
        print("Invalid input! Please enter an integer.")

if __name__ == "__main__":
    main()
