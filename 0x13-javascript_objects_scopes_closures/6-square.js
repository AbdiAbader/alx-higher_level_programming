#!/usr/bin/node
const Ss = require('./5-square');
module.exports = class Square extends Ss {
  charPrint (c = 'X') {
    for (let i = 0; i < this.height; i++) {
      let x = '';
      for (let j = 0; j < this.width; j++) {
        x = x + c;
      }
      console.log(x);
    }
  }
};
