#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./3-starwars_title.js ID');
  process.exit(1);
}
const url = 'https://swapi-api.hbtn.io/api/films/' + process.argv[2];
request(url, (err, body) => {
  if (err) {
    console.log(err);
  }
  console.log(JSON.parse(body).title);
});
