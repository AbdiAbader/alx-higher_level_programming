#!/usr/bin/node

if (isNaN(parseInt(process.argv[2]))) {
  console.log('Missing size');
} else {
  for (let i = 0; i < process.argv[2]; i++) {
    let x = '';
    for (let j = 0; j < process.argv[2]; j++) {
      x = x + 'X';
    }
    console.log(x);
  }
}
