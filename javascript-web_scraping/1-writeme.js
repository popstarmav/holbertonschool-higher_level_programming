#!/usr/bin/node
const fs = require('fs');

function writeFileCallback(err) {
  if (err) {
    console.log(err);
  }
}

// Check if the correct number of arguments is provided
if (process.argv.length !== 4) {
  console.error('Usage: ./1-writeme.js <file-path> <string-to-write>');
  process.exit(1); // Exit with an error code
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

// Write the content to the file in utf-8
fs.writeFile(filePath, contentToWrite, writeFileCallback);
