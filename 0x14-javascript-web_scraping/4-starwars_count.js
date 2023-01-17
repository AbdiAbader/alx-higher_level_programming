#!/usr/bin/node

const request = require('request');

if (process.argv.length < 3) {
  console.log('Usage: ./4-starwars_count.js URL');
  process.exit(1);
}
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  }
  let count = 0;
  const films = JSON.parse(body).results;
  for (const film of films) {
    for (const character of film.characters) {
      if (character.includes('18')) {
        count++;
      }
    }
  }
  console.log(count);
});
