#!/usr/bin/node
const intArray = process.argv.splice(2);
const arrLength = intArray.length;
let result, i, j;

function secondLargest (intArray) {
  result = intArray.slice(0);
  i = Math.max.apply(Math, result);
  i = i - 1;

  while (i > 0) {
    for (j = 0; j < arrLength; j++) {
      if (parseInt(i) === parseInt(result[j])) {
        return result[j];
      }
    }
    i--;
  }
}

if (arrLength > 1) {
  console.log(secondLargest(intArray));
} else {
  console.log(0);
}
