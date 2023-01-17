#!/usr/bin/node

const request = require('request');
const fs = require('fs');
if (process.argv.length < 4) {
  console.log('Usage: ./6-completed_tasks.js USER_ID');
  process.exit(1);
}
request('https://jsonplaceholder.typicode.com/todos', (err, body) => {
  if (err) {
    console.log(err);
  } else {
    const json = JSON.parse(body.body);
    const dict = {};
    for (const task of json) {
      if (task.completed) {
        if (task.userId in dict) {
          dict[task.userId] += 1;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
    for (const key in dict) {
      console.log(key + ': ' + dict[key]);
    }
  }
});
