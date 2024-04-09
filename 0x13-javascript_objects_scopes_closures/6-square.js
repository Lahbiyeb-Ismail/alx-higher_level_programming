#!/usr/bin/node

const Square5 = require('./5-square.js');

class Square extends Square5 {
  charPrint (c) {
    if (c === undefined) {
      this.print();
    } else {
      for (let i = 0; i < this.height; i++) {
        let str = '';
        for (let j = 0; j < this.width; j++) {
          str += c;
        }

        console.log(str);
      }
    }
  }
}

module.exports = Square;
