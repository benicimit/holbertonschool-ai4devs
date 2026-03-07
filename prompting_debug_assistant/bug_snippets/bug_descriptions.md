## Bug 1 – bug1.py

**Type:** Syntax error

**Intended Behavior:**  
The factorial function should compute the factorial of a given number using recursion.  
For example, `factorial(5)` should return `120` and `factorial(0)` should return `1`.

**Issue:**  
The code contains syntax errors that prevent the Python program from running.

**Notes:**  
- The line `if n == 0` is missing the required colon (`:`).  
- The line `return n factorial(n - 1)` is missing the multiplication operator `*`.  
- The correct line should be `return n * factorial(n - 1)`.

---

## Bug 2 – bug2.c

**Type:** Logical error

**Intended Behavior:**  
The program should calculate the sum of all elements in an integer array.  
For example, the array `[1,2,3,4,5]` should produce the result `15`.

**Issue:**  
The code assigns each array element to `sum` instead of adding it to the running total.

**Notes:**  
- The incorrect line is `sum = arr[i];`.  
- It should be `sum += arr[i];` so each element is added to the total.

---

## Bug 3 – bug3.cpp

**Type:** Runtime exception

**Intended Behavior:**  
The program should divide two integers and print the result.  
For example, dividing `10` by `2` should output `5`.

**Issue:**  
The code performs division by zero, which causes a runtime error.

**Notes:**  
- The variable `denominator` is set to `0`.  
- The line `int result = numerator / denominator;` executes without checking the value.  
- The program should verify that `denominator != 0` before performing the division.

---

## Bug 4 – bug4.java

**Type:** Off-by-one error

**Intended Behavior:**  
The program should print the numbers from `1` to `10` inclusive.

**Issue:**  
The loop stops before reaching `10`.

**Notes:**  
- The loop uses `i < 10`, which prints numbers `1` through `9`.  
- The correct condition should be `i <= 10`.

---

## Bug 5 – bug5.js

**Type:** Misuse of data types

**Intended Behavior:**  
The program should calculate the sum of numbers stored as strings in an array.  
For example, `["1","2","3","4","5"]` should produce the number `15`.

**Issue:**  
The code adds string values directly, which causes string concatenation instead of numeric addition.

**Notes:**  
- The line `sum += num;` treats `num` as a string.  
- The values should be converted using `Number(num)` or `parseInt(num)` before adding.

---

## Bug 6 – bug6.php

**Type:** Logical error

**Intended Behavior:**  
The `isPrime` function should determine whether a number is prime.  
For example, `isPrime(7)` should return `true` and `isPrime(9)` should return `false`.

**Issue:**  
The function incorrectly returns `true` when the number is divisible by another number.

**Notes:**  
- The incorrect line is `if ($n % $i == 0) return true;`.  
- If a number is divisible by another number, it is not prime.  
- The correct statement should be `return false`.