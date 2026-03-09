# Bug 1: Python - Syntax Error
# Type: Syntax Error
# Intended Behavior: Compute factorial of a number using recursion.
# Issue: Missing colon after 'if n == 0' and missing '*' in recursive return.
# Notes: Should handle n >= 0; base case n==0 returns 1.

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