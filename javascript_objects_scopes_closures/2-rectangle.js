#!/usr/bin/node

class Rectangle {
  constructor(width, height) {
    this.width = width > 0 ? width : null;
    this.height = height > 0 ? height : null;
  }
}

module.exports = Rectangle;
