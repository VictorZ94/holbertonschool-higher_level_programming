#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const dict = {};
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const task of info) {
      if (task.completed === true) {
        if (task.userId in dict) {
          dict[task.userId] += 1;
        } else {
          dict[task.userId] = 1;
        }
      }
    }
  }
  console.log(dict);
});
