#!/usr/bin/node
// Using const for constant values
const arg = process.argv[2];

// Convert the argument to an integer
const size = parseInt(arg);

// Checking if the conversion was successful and printing the square
if (!isNaN(size)) {
  for (let i = 0; i < size; i++) {
    console.log('X'.repeat(size));
  }
} else {
  console.log('Missing size');
}
