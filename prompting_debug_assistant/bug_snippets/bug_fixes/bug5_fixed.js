// Type: Misuse of Data Types
// Intended Behavior: Add two numbers and print the sum.
// Issue: Concatenating strings instead of adding numbers.
// Notes: Should convert strings to numbers before adding.
let num1 = "5";
let num2 = "10";

let sum = parseInt(num1) + parseInt(num2);  // Fixed: added parseInt to convert strings to numbers

console.log("Sum: " + sum);