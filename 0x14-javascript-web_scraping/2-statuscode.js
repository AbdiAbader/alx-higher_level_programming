#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./2-statuscode.js URL');
  process.exit(1);
}
request(process.argv[2], (err, response) => {
  if (err) {
    console.log(err);
  } else {
    console.log('code: ' + response.statusCode);
  }
}
);
