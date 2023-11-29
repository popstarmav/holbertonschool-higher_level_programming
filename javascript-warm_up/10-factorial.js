#!/usr/bin/node
// Define the factorial function recursively
const factorial = (n) => {
  if (isNaN(n) || n < 0) {
    return 1; // Factorial of NaN or negative numbers is 1
  }
  if (n === 0 || n === 1) {
    return 1; // Factorial of 0 or 1 is 1
  }
  return n * factorial(n - 1);
};

// Using const for constant values
const arg = process.argv[2];

// Convert the argument to an integer
const num = parseInt(arg);

// Checking if the conversion was successful and printing the result
if (!isNaN(num)) {
  console.log(factorial(num));
} else {
  console.log('Invalid input. Please provide a non-negative integer.');
}
