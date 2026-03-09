// Type: Misuse of Data Types
// Intended Behavior: Sum numeric values stored as strings.
// Issue: Strings concatenated instead of converted and added.
// Notes: Convert each element with parseInt/Number before adding.

let numbers = ["1", "2", "3", "4", "5"];
let sum = 0;

for (let num of numbers) {
    sum += num;  // This concatenates strings instead of adding numbers
}

console.log("Sum:", sum);