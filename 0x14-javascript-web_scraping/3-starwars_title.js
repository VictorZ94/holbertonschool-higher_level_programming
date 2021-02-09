#!/usr/bin/node
const request = require('request');
const id = process.argv[2];
const url = 'https://swapi-api.hbtn.io/api/films/' + id;
request(url, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  const bodyParsed = JSON.parse(body);
  console.log(bodyParsed.title);
});
