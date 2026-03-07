## Bug 1 – bug1.py

**Type:** Syntax error

**Intended Behavior:**  
The factorial function should compute the factorial of a given number using recursion. For example, `factorial(5)` should return `120`, `factorial(0)` should return `1`, and the function should handle non-negative integers correctly.

**Issue:**  
The code contains a syntax error due to a missing colon after the `if` condition, which prevents the Python code from executing and causes a SyntaxError.

**Notes:**  
The bug is in the line `if n == 0` which lacks the required colon (`:`) for Python's if statement syntax. This makes the code invalid and unable to run.

---

## Bug 2 – bug2.c

**Type:** Logical error

**Intended Behavior:**  
The function should calculate the sum of all elements in an integer array. For example, with the array `[1, 2, 3, 4, 5]`, it should return `15`.

**Issue:**  
The code incorrectly uses multiplication instead of addition in the loop, causing it to compute the product of array elements instead of their sum.

**Notes:**  
The bug is in the line `sum *= arr[i];`. It should be `sum += arr[i];` to properly accumulate the sum. The current implementation results in a product (e.g., 120 instead of 15 for the example array).

---

## Bug 3 – bug3.cpp

**Type:** Runtime exception

**Intended Behavior:**  
The program should perform division of two integers and display the result safely. It should handle cases where the denominator might be zero by either checking beforehand or providing appropriate error handling.

**Issue:**  
The code attempts to divide by zero, which causes a runtime exception (division by zero error) and crashes the program.

**Notes:**  
The bug occurs because `denominator` is set to `0`, and the line `int result = numerator / denominator;` performs division without checking if the denominator is zero. In C++, this typically results in undefined behavior or an exception.

---

## Bug 4 – bug4.java

**Type:** Off-by-one error

**Intended Behavior:**  
The program should print the numbers from 1 to 10 inclusive, each on a new line. For example, it should output: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

**Issue:**  
The loop condition uses `i < 10` instead of `i <= 10`, causing the loop to terminate before printing the number 10, resulting in only numbers 1 through 9 being printed.

**Notes:**  
The bug is in the loop condition `for (int i = 1; i < 10; i++)`. It should be `for (int i = 1; i <= 10; i++)` to include 10 in the output. This is a classic off-by-one error in loop bounds.

---

## Bug 5 – bug5.js

**Type:** Misuse of Data Types

**Intended Behavior:**  
The code should calculate the sum of numeric values stored as strings in an array. For example, with `["1", "2", "3", "4", "5"]`, it should return `15` after converting strings to numbers.

**Issue:**  
The code treats string elements as numbers without proper conversion, leading to string concatenation instead of numeric addition, resulting in `"12345"` instead of `15`.

**Notes:**  
The bug is in the line `sum += num;`, where `num` is a string. JavaScript's `+` operator concatenates strings, so it doesn't perform numeric addition. The strings need to be converted to numbers using `parseInt(num)` or `Number(num)` before adding.

---

## Bug 6 – bug6.php

**Type:** Logical error

**Intended Behavior:**  
The `isPrime` function should determine if a given integer is a prime number. For example, `isPrime(7)` should return `true`, `isPrime(9)` should return `false`, and `isPrime(1)` should return `false`.

**Issue:**  
The function incorrectly returns `true` when the number is divisible by another number, instead of returning `false`, leading to wrong results for composite numbers.

**Notes:**  
The bug is in the line `if ($n % $i == 0) return true;`. It should be `if ($n % $i == 0) return false;` to indicate that if the number is divisible by any `i`, it's not prime. The current logic inverts the boolean return value.