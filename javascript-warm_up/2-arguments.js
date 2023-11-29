#!/usr/bin/node
// Check number of arguments and print message
if (process.argv.length === 2) {
    console.log('No argument');
} else if (process.argv.length === 3) {
    console.log('Argument found');
} else {
    console.log('Arguments found');
}
