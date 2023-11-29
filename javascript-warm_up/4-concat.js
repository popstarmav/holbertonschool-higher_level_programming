#!/usr/bin/node
// Using const for constant values
const args = process.argv.slice(2);

// Checking if arguments passed and print the specified format
if (args.length >= 2) {
  console.log(`${args[0]} is ${args[1]}`);
} else {
  console.log('Not enough arguments');
}
