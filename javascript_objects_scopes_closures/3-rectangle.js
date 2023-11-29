#!/usr/bin/node
const validRectangle = new Rectangle(5, 3);
validRectangle.print();

const invalidRectangle = new Rectangle(0, 4);
invalidRectangle.print(); // This won't print anything due to the invalid dimensions
