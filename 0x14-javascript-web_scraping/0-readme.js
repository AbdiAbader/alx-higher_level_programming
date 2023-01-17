#!/usr/bin/node
if (process.argv.length < 3) {
  console.log('Usage: ./0-readme.js FILE');
  process.exit(1);
}
const fs = require('fs');
fs.readFile(process.argv[2], 'utf8', (err, data) => {
    if (err) {
        console.log(err);
    } else {
        console.log(data);
    }
    });
