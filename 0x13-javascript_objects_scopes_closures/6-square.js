#!/usr/bin/node
const SquareParent = require('./5-square');
class Square extends SquareParent {
  charPrint(c) {
    if (c !== undefined) {
      for (let i = 0; i < this.width; i++) {
        console.log(c.repeat(this.height));
      }
    }
    else {
      this.print();
    }
  }
}

module.exports = Square;
