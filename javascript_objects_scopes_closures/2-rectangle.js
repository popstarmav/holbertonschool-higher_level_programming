#!/usr/bin/node
const validRectangle = new Rectangle(5, 3);
console.log(validRectangle.width);  // Output: 5
console.log(validRectangle.height); // Output: 3

const invalidRectangle = new Rectangle(0, 4);
console.log(invalidRectangle.width);  // Output: null
console.log(invalidRectangle.height); // Output: null
