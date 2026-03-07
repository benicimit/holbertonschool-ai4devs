// Intended to calculate the sum of numbers in an array
// Bug: Misuse of data types - treating strings as numbers without conversion

let numbers = ["1", "2", "3", "4", "5"];
let sum = 0;

for (let num of numbers) {
    sum += num;  // This concatenates strings instead of adding numbers
}

console.log("Sum:", sum);