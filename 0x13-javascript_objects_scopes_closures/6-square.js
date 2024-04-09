#!/usr/bin/node

const Square5 = require('./5-square.js');

class Square extends Square5 {
  charPrint(c) {
    let char = '';

    c ? (char = c) : (char = 'X');

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
