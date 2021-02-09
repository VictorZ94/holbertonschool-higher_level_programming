#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let counter = 0;
request(url, function (error, response, body) {
  if (!error && response.statusCode === 200) {
    const info = JSON.parse(body);
    for (const movie of info.results) {
      for (const character of movie.characters) {
        if (character.includes('18')) {
          counter++;
        }
      }
    }
  }
  console.log(counter);
});
