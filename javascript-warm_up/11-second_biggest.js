#!/usr/bin/node
// Using const for constant values
const args = process.argv.slice(2);

// Convert the arguments to integers
const numbers = args.map(Number);

// Checking if there are at least two arguments
if (numbers.length < 2) {
  console.log(0);
} else {
  // Sorting the numbers in descending order
  const sortedNumbers = numbers.sort((a, b) => b - a);

  // Finding and printing the second biggest integer
  console.log(sortedNumbers[1]);
}
