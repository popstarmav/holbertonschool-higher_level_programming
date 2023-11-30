class Rectangle {
  constructor(width, height) {
    if (width !== undefined && height !== undefined) {
      if (width > 0 && height > 0) {
        this.width = width;
        this.height = height;
      } else {
        this.width = {};
        this.height = {};
      }
    } else if (width !== undefined && height === undefined) {
      this.width = width;
      this.height = {};
    } else {
      this.width = {};
      this.height = {};
    }
  }
}

module.exports = Rectangle;
