# Bug Description Documentation

---

## Bug 1 – bug1.py

**Type:** Syntax Error

**Intended Behavior:**  
The `factorial` function should correctly compute the factorial of a non-negative integer using recursion. Specifically:
- When called with `n = 0`, it should return `1` (the base case, as 0! = 1)
- When called with `n = 5`, it should return `120` (5! = 5 × 4 × 3 × 2 × 1)
- The function should handle all non-negative integers without throwing syntax errors that prevent execution

**Issue:**  
The code contains multiple syntax errors that prevent Python from executing the program:
1. The `if` statement on line 5 is missing a colon (`:`) after the condition
2. The return statement on line 8 is missing the multiplication operator (`*`) between `n` and the recursive call

**Notes:**  
- **Line 5 error**: `if n == 0` should be `if n == 0:`
- **Line 8 error**: `return n factorial(n - 1)` should be `return n * factorial(n - 1)`
- These syntax errors will cause a `SyntaxError` exception before any code executes

---

## Bug 2 – bug2.c

**Type:** Logical Error

**Intended Behavior:**  
The program should calculate and display the sum of all elements in an integer array. Specifically:
- For the array `[1, 2, 3, 4, 5]`, the sum should be `15` (1 + 2 + 3 + 4 + 5)
- It should accumulate each element by adding it to the running total
- The result should be printed as `Sum of array elements: 15`

**Issue:**  
The code incorrectly uses the multiplication assignment operator (`*=`) instead of the addition assignment operator (`+=`), causing the sum to compute incorrectly:
- First iteration: `sum = 0 * 1 = 0`
- Second iteration: `sum = 0 * 2 = 0`
- All subsequent iterations produce `0`
- Final result: `0` instead of `15`

**Notes:**  
- **Buggy line**: `sum *= arr[i];` on line 11
- **Correct line**: `sum += arr[i];`
- The operator `*=` performs multiplication and assignment, whereas `+=` performs addition and assignment
- This is a common copy-paste or typo error that produces logically valid C code but incorrect results

---

## Bug 3 – bug3.cpp

**Type:** Runtime Exception

**Intended Behavior:**  
The program should perform integer division of two numbers and display the result. Specifically:
- When dividing numerator `10` by denominator `2`, it should output `The result of division is: 5`
- The program should safely handle the division operation
- It should gracefully handle or prevent division by zero scenarios

**Issue:**  
The code performs division by zero, which is undefined behavior in C++ and causes a runtime exception (typically an arithmetic exception) that crashes the program:
- The variable `denominator` is initialized to `0` on line 6
- The division operation `numerator / denominator` on line 10 attempts to divide by zero
- This causes the program to crash with a runtime error instead of producing a result

**Notes:**  
- **Problematic line**: `int result = numerator / denominator;` on line 10
- **Root cause**: `denominator` is set to `0` without validation
- **Prevention**: Before division, check `if (denominator != 0)` to prevent runtime exceptions
- Division by zero is undefined in both C and C++ and leads to undefined behavior or program termination

---

## Bug 4 – bug4.java

**Type:** Off-by-one Error

**Intended Behavior:**  
The program should print the integers from 1 to 10 (inclusive), each on a separate line. Specifically:
- The output should contain exactly 10 lines with values: `1, 2, 3, 4, 5, 6, 7, 8, 9, 10`
- All numbers from 1 through 10 must be printed
- The program demonstrates correct loop bounds and exits gracefully

**Issue:**  
The loop condition uses `i < 10` instead of `i <= 10`, causing the loop to terminate before printing the number 10:
- Loop iterations: i = 1, 2, 3, 4, 5, 6, 7, 8, 9 (stops before i = 10)
- Output produced: `1, 2, 3, 4, 5, 6, 7, 8, 9` (missing 10)
- One element is missing from the expected output

**Notes:**  
- **Buggy line**: `for (int i = 1; i < 10; i++)` on line 6
- **Correct line**: `for (int i = 1; i <= 10; i++)`
- This is a classic off-by-one error in loop termination conditions
- The operator `<` excludes the boundary value, while `<=` includes it

---

## Bug 5 – bug5.js

**Type:** Misuse of Data Types

**Intended Behavior:**  
The program should calculate the numeric sum of values stored as strings in an array. Specifically:
- For the array `["1", "2", "3", "4", "5"]`, the sum should be the number `15`
- The program should convert string values to numbers before performing arithmetic
- The output should be `Sum: 15` (not `Sum: 012345`)

**Issue:**  
The code performs string concatenation instead of numeric addition due to type coercion in JavaScript:
- The array contains string elements: `["1", "2", "3", "4", "5"]`
- The line `sum += num;` concatenates strings when `num` is a string type
- Instead of adding: 1 + 2 + 3 + 4 + 5 = 15
- Result is: "0" + "1" + "2" + "3" + "4" + "5" = "012345"
- The operator `+` in JavaScript concatenates when either operand is a string

**Notes:**  
- **Problematic line**: `sum += num;` on line 6 treats the string as a number
- **Solution**: Convert strings to numbers using `parseInt(num)`, `Number(num)`, or `parseFloat(num)` before adding
- **Better approach**: `sum += parseInt(num);` or `sum += Number(num);`
- JavaScript's type coercion can be a source of subtle bugs; always be explicit about type conversions

---

## Bug 6 – bug6.php

**Type:** Logical Error

**Intended Behavior:**  
The `isPrime` function should correctly determine whether a given integer is a prime number. Specifically:
- `isPrime(7)` should return `true` (7 is prime)
- `isPrime(9)` should return `false` (9 is composite: 9 = 3 × 3)
- `isPrime(1)` should return `false` (1 is not considered prime by convention)
- Composite numbers should be identified correctly to prevent false positives

**Issue:**  
The function returns the inverse of the expected boolean value when a divisor is found:
- When the loop finds that `$n % $i == 0` (meaning `$n` is divisible by `$i`), it returns `true`
- This is backwards: divisibility should indicate the number is NOT prime
- For `isPrime(9)`: The function finds 9 % 3 == 0 and returns `true`, when it should return `false`
- Prime testing is inverted, causing false positives for all composite numbers

**Notes:**  
- **Buggy line**: `if ($n % $i == 0) return true;` on line 14
- **Correct line**: `if ($n % $i == 0) return false;`
- When a number is divisible by another number, it is composite (not prime)
- The conditional logic is inverted, returning `true` for divisibility instead of `false`
