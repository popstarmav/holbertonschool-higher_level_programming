#!/usr/bin/node
const fs = require('fs');

function writeToFile(filePath, contentToWrite) {
  fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
    if (error) {
      console.error(error); // Print the error object
    } else {
      console.log(`Content successfully written to ${filePath}`);
    }
  });
}

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./write_file.js <file-path> <string-to-write>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Call the function to write to the file
writeToFile(filePath, contentToWrite);
