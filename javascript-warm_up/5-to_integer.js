#!/usr/bin/node
// Using const for constant values
const arg = process.argv[2];

// Convert the argument to an integer
const number = parseInt(arg);

// Checking if the conversion was successful and printing the result
if (!isNaN(number)) {
  console.log(`My number: ${number}`);
} else {
  console.log('Not a number');
}
