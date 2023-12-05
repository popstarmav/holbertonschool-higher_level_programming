#!/usr/bin/node
const fs = require('fs');

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./write_file.js <file-path> <string-to-write>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the content to the file in utf-8
fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
  if (error) {
    console.error(error); // Print the error object
  } else {
    console.log(`Content successfully written to ${filePath}`);
  }
});

// Read the content of the file to verify the output
fs.readFile(filePath, 'utf-8', (readError, readData) => {
  if (readError) {
    console.error(`Error reading the file: ${readError}`);
  } else {
    console.log('Correct output - text:', JSON.stringify(readData));
  }
});
