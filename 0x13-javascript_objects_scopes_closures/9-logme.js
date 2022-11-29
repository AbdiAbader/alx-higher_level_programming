#!/usr/bin/node

let num = 0;
exports.logMe = function (item) {
  function print () {
    console.log(num + ': ' + item);
    num += 1;
  }
  print();
};
