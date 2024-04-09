#!/usr/bin/node

const Square5 = require('./5-rectangle.js');

class Square extends Square5 {
  charPrint (c) {
    const char = c ? c : 'X';

    for (let i = 0; i < this.height; i++) {
      let str = '';
      for (let j = 0; j < this.width; j++) {
        str += char;
      }

      console.log(str);
    }
  }
}

module.exports = Square;
