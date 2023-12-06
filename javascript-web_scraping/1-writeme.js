#!/usr/bin/node
const fs = require('fs');

if (process.argv.length !== 4) {
  console.error('Usage: ./writeToFile.js <file-path> <string-to-write>');
  process.exit(1);
}

const filePath = process.argv[2];
const contentToWrite = process.argv[3];

fs.writeFile(filePath, contentToWrite, 'utf-8', (error) => {
  if (error) {
    console.error(error);
  } else {
    console.log(`Content successfully written to ${filePath}`);
  }
});
