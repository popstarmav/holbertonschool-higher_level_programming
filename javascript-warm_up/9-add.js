#!/usr/bin/node
// Define the add function
const add = (a, b) => a + b;

// Using const for constant values
const arg1 = process.argv[2];
const arg2 = process.argv[3];

// Convert the arguments to integers
const num1 = parseInt(arg1);
const num2 = parseInt(arg2);

// Checking if the conversion was successful and printing the result
if (!isNaN(num1) && !isNaN(num2)) {
  console.log(add(num1, num2));
} else {
  console.log('Invalid input. Please provide two integers.');
}
