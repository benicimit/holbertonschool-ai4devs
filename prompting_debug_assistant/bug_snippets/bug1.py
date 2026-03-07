# Bug 1: Python - Syntax Error
# Intended to calculate the factorial of a number using recursion.
# Bug: Missing colon after 'if n == 0'

def factorial(n):
    if n == 0  # Missing colon here
        return 1
    else:
        return n * factorial(n - 1)

# Test the function
if __name__ == "__main__":
    num = 5
    result = factorial(num)
    print(f"Factorial of {num} is {result}")