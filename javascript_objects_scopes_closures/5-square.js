#!/usr/bin/node

class Shape {
  constructor (sideLength) {
    this.sideLength = sideLength;
  }

  print () {
    if (this.sideLength !== null) {
      for (let i = 0; i < this.sideLength; i++) {
        console.log('X'.repeat(this.sideLength));
      }
    }
  }

  double () {
    if (this.sideLength !== null) {
      this.sideLength *= 2;
    }
  }
}

class Square extends Shape {}

module.exports = Square;
