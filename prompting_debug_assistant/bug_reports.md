# Bug Reports

This document summarizes the findings from debugging each buggy snippet, including root causes, resolutions, and lessons learned.

## Bug Report – bug1.py
- **File Name**: bug1.py (fixed as bug1_fixed.py)
- **Summary**: Syntax error in recursive factorial function preventing execution.
- **Root Cause**: Missing colon after `if n == 0` and missing `*` operator in recursive return.
- **Resolution**: AI suggested adding colon and `*` operator. No manual edits needed beyond AI suggestion.
- **Lessons Learned**: Syntax errors can halt execution; always check for colons and operators in Python.

## Bug Report – bug2.c
- **File Name**: bug2.c (fixed as bug2_fixed.c)
- **Summary**: Logical error in array summation, computing product instead of sum.
- **Root Cause**: Incorrect use of `*=` instead of `+=` in the loop.
- **Resolution**: AI suggested changing `*=` to `+=`. No manual edits needed.
- **Lessons Learned**: Operator misuse can lead to incorrect logic; verify accumulation operations.

## Bug Report – bug3.cpp
- **File Name**: bug3.cpp (fixed as bug3_fixed.cpp)
- **Summary**: Runtime error due to division by zero.
- **Root Cause**: No check for zero denominator before division.
- **Resolution**: AI suggested adding `if (denominator != 0)` check. No manual edits needed.
- **Lessons Learned**: Handle edge cases like division by zero to prevent crashes.

## Bug Report – bug4.java
- **File Name**: bug4.java (fixed as Bug4.java)
- **Summary**: Off-by-one error in loop, excluding the upper bound.
- **Root Cause**: Loop condition `i < 10` stops at 9 instead of 10.
- **Resolution**: AI suggested changing to `i <= 10`. Manual edit: Renamed file to `Bug4.java` for Java compilation (AI-generated fix applied, manual file rename for naming convention).
- **Lessons Learned**: Off-by-one errors are common in loops; use inclusive bounds carefully.

## Bug Report – bug5.js
- **File Name**: bug5.js (fixed as bug5_fixed.js)
- **Summary**: Data type misuse, concatenating strings instead of adding numbers.
- **Root Cause**: Using `+` on strings without conversion to numbers.
- **Resolution**: AI suggested `parseInt(num)` for conversion. No manual edits needed.
- **Lessons Learned**: Ensure correct data types for operations; convert strings to numbers when needed.

## Bug Report – bug6.php
- **File Name**: bug6.php (fixed as bug6_fixed.php)
- **Summary**: Logical error in prime check, returning true for non-prime.
- **Root Cause**: Returning `true` when divisor found, inverting the logic.
- **Resolution**: AI suggested changing `return true;` to `return false;`. No manual edits needed.
- **Lessons Learned**: Double-check conditional logic in algorithms like primality tests.