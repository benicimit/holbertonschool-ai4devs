## Bug 1 – bug1.py

**Type:** Syntax error

**Intended Behavior:**  
The factorial function should compute the factorial of a given number using recursion. For example, `factorial(5)` should return `120`, `factorial(0)` should return `1`, and the function should correctly handle non-negative integers.

**Issue:**  
The code contains syntax errors that prevent the Python program from executing.

**Notes:**  
- The line `if n == 0` is missing the required colon (`:`) used in Python conditional statements.  
- The line `return n factorial(n - 1)` is missing the multiplication operator (`*`).  
- The correct recursive statement should be `return n * factorial(n - 1)`.

---

## Bug 2 – bug2.c

**Type:** Logical error

**Intended Behavior:**  
The program should calculate the sum of all elements in an integer array. For example, with the array `[1, 2, 3, 4, 5]`, the program should return `15` by adding each element to a running total.

**Issue:**  
The code overwrites the `sum` variable during each iteration instead of adding the array values to it. As a result, the final value of `sum` becomes only the last element of the array.

**Notes:**  
- The incorrect line is `sum = arr[i];`.  
- It should be `sum += arr[i];` so that each element is added to the existing total.  
- With the bug, the program outputs `5` instead of the correct total `15`.

---

## Bug 3 – bug3.cpp

**Type:** Runtime exception

**Intended Behavior:**  
The program should divide two integers and display the result. For example, dividing `10` by `2` should output `5`.

**Issue:**  
The program performs division by zero, which causes a runtime error and crashes the program because division by zero is undefined in C++.

**Notes:**  
- The variable `denominator` is set to `0`.  
- The line `int result = numerator / denominator;` performs division without checking the value of the denominator.  
- The program should check that `denominator != 0` before performing the division.

---

## Bug 4 – bug4.java

**Type:** Off-by-one error

**Intended Behavior:**  
The program should print the numbers from `1` to `10` inclusive, each on a new line.

**Issue:**  
The loop condition stops the loop too early because it uses `i < 10`, which excludes the number `10`.

**Notes:**  
- The incorrect loop is `for (int i = 1; i < 10; i++)`.  
- This prints only numbers `1` through `9`.  
- The correct loop condition should be `for (int i = 1; i <= 10; i++)` so that the number `10` is also printed.

---

## Bug 5 – bug5.js

**Type:** Misuse of Data Types

**Intended Behavior:**  
The program should calculate the sum of numeric values stored as strings in an array. For example, with `["1", "2", "3", "4", "5"]`, the program should convert each string to a number and return `15`.

**Issue:**  
The code adds string values directly without converting them to numbers, which causes JavaScript to perform string concatenation instead of numeric addition.

**Notes:**  
- The problematic line is `sum += num;`.  
- Because `num` is a string, the `+` operator concatenates the values, resulting in `"12345"` instead of `15`.  
- The values should be converted using `Number(num)` or `parseInt(num)` before adding them.

---

## Bug 6 – bug6.php

**Type:** Logical error

**Intended Behavior:**  
The `isPrime` function should determine whether a given integer is a prime number. For example, `isPrime(7)` should return `true`, `isPrime(9)` should return `false`, and `isPrime(1)` should return `false`.

**Issue:**  
The function incorrectly returns `true` when the number is divisible by another number, which causes composite numbers to be identified as prime.

**Notes:**  
- The incorrect line is `if ($n % $i == 0) return true;`.  
- If a number is divisible by another number, it is **not** prime.  
- The correct statement should be `if ($n % $i == 0) return false;`.