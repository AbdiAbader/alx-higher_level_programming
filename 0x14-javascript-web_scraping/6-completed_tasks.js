#!/usr/bin/node

const request = require('request');
if (process.argv.length < 3) {
  console.log('Usage: ./6-completed_tasks.js URL');
  process.exit(1);
}
request(process.argv[2], (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const completed = {};
    for (const task of tasks) {
      if (task.completed) {
        if (completed[task.userId]) {
          completed[task.userId]++;
        } else {
          completed[task.userId] = 1;
        }
      }
    }
    console.log(completed);
  }
}
);
