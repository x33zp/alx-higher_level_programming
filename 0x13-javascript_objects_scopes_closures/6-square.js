#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c) {
    for (let i = 0; i < this.width; i++) {
      c ? console.log('C'.repeat(this.width)) : console.log('X'.repeat(this.width));
    }
  }
}

module.exports = Square;
