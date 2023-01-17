#!/usr/bin/node

const request = require('request');
const fs = require('fs');
if (process.argv.length < 4) {
  console.log('Usage: ./5-request_store.js URL FILE');
  process.exit(1);
}
request(process.argv[2], (err, body) => {
  if (err) {
    console.log(err);
  } else {
    fs.writeFile(process.argv[2], body, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  }
});
