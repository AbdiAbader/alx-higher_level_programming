#!/usr/bin/node
const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./3-starwars_title.js ID');
  process.exit(1);
}
request('https://swapi-api.hbtn.io/api/films/' + process.argv[2], (err, response, body) => {
    if (err) {
        console.log(err);
    } else {
        console.log(JSON.parse(body).title);
    }
});