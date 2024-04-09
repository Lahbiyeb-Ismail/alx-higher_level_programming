#!/usr/bin/node

const Rectangle = require('./4-rectangle.js');

class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < size; i++) {
        let str = '';
        for (let j = 0; j < size; j++) {
          str += c;
        }

        console.log(str);
      }
    } else {
      this.print();
    }
  }
}

module.exports = Square;
