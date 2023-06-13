#!/usr/bin/node

/*
 * a class Square that defines a square and inherits from Square of 5-square.js
 */
const Rectangle = require('./5-square.js');

class Square extends Rectangle {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let row = '';
        for (let j = 0; j < this.width; j++) {
          row += 'C';
        }
        console.log(row);
      }
    }
  }
}
module.exports = Square;
