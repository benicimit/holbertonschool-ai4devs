## Bug 1 – bug1.py

**Type:** Syntax error

**Intended Behavior:**  
The factorial function should compute the factorial of a given number using recursion. For example, `factorial(5)` should return `120`, `factorial(0)` should return `1`, and the function should handle non-negative integers correctly.

**Issue:**  
The code contains multiple syntax errors: a missing colon after the `if` condition and a missing multiplication operator in the recursive return statement, which prevent the Python code from executing and cause SyntaxErrors.

**Notes:**  
- The line `if n == 0` lacks the required colon (`:`) for Python's if statement syntax.  
- The line `return n factorial(n - 1)` is missing the `*` operator and should be `return n * factorial(n - 1)` to perform multiplication.

---

## Bug 2 – bug2.c

**Type:** Logical error

**Intended Behavior:**  
The function should calculate the sum of all elements in an integer array. For example, with the array `[1, 2, 3, 4, 5]`, it should return `15` by adding each element to an accumulator.

**Issue:**  
The code uses assignment instead of addition in the loop, causing the `sum` variable to be overwritten with each array element instead of accumulating their values, resulting in `sum` holding only the value of the last element.

**Notes:**  
The bug is in the line `sum = arr[i];`. It should be `sum += arr[i];` to properly add each element to the running total. The current implementation sets `sum` to `5` (the last element) instead of `15`.

---

## Bug 3 – bug3.cpp

**Type:** Runtime exception

**Intended Behavior:**  
The program should perform division of two integers and display the result. For example, dividing `10` by `2` should output `5`.

**Issue:**  
The code attempts to divide by zero, which causes a runtime exception (division by zero error) and crashes the program, as division by zero is undefined in C++.

**Notes:**  
The bug occurs because `denominator` is set to `0`, and the line `int result = numerator / denominator;` performs division without any validation. The program should check if `denominator != 0` before dividing.

---

## Bug 4 – bug4.java

**Type:** Off-by-one error

**Intended Behavior:**  
The program should print the numbers from 1 to 10 inclusive, each on a new line. For example, it should output the sequence: 1, 2, 3, 4, 5, 6, 7, 8, 9, 10.

**Issue:**  
The loop condition uses `i < 10` instead of `i <= 10`, causing the loop to terminate before printing the number 10, resulting in only numbers 1 through 9 being printed and missing the upper bound.

**Notes:**  
The bug is in the loop condition `for (int i = 1; i < 10; i++)`. It should be `for (int i = 1; i <= 10; i++)` to include 10 in the output. This is a classic off-by-one error in loop termination conditions.

---

## Bug 5 – bug5.js

**Type:** Misuse of Data Types

**Intended Behavior:**  
The code should calculate the sum of numeric values stored as strings in an array. For example, with `["1", "2", "3", "4", "5"]`, it should convert each string to a number and return `15` as the total sum.

**Issue:**  
The code treats string elements as numbers without proper conversion, leading to string concatenation instead of numeric addition, resulting in the string `"12345"` instead of the number `15`.

**Notes:**  
The bug is in the line `sum += num;`, where `num` is a string. JavaScript's `+` operator concatenates strings when operands are strings. The strings need to be converted to numbers using `parseInt(num)` or `Number(num)` before adding to perform arithmetic addition.

---

## Bug 6 – bug6.php

**Type:** Logical error

**Intended Behavior:**  
The `isPrime` function should determine if a given integer is a prime number. For example, `isPrime(7)` should return `true`, `isPrime(9)` should return `false`, and `isPrime(1)` should return `false`.

**Issue:**  
The function incorrectly returns `true` when the number is divisible by another number, instead of returning `false`, leading to wrong results for composite numbers like 9, which would be reported as prime.

**Notes:**  
The bug is in the line `if ($n % $i == 0) return true;`. It should be `if ($n % $i == 0) return false;` to indicate that if the number is divisible by any `i`, it's not prime. The current logic inverts the boolean return value, causing false positives.