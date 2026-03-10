// Type: Misuse of Data Types (Fixed)
// Intended Behavior: Sum numeric values stored as strings.
// Issue: Fixed - Convert each element with parseInt before adding.
// Notes: Now converts strings to numbers before adding.

let numbers = ["1", "2", "3", "4", "5"];
let sum = 0;

for (let num of numbers) {
    sum += parseInt(num);  // Fixed: added parseInt to convert string to number
}

console.log("Sum:", sum);