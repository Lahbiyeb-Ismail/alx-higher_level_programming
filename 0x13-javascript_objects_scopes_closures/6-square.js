#!/usr/bin/node

const Square5 = require('./5-rectangle.js');

class Square extends Square5 {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    if (c) {
      for (let i = 0; i < this.size; i++) {
        let str = '';
        for (let j = 0; j < this.size; j++) {
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
