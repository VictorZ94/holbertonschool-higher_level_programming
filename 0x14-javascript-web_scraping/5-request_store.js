#!/usr/bin/node
const request = require('request');
const fs = require('fs');
const url = process.argv[2];
const pathFile = process.argv[3];
request(url, { encoding: 'utf-8' }, function (error, response, body) {
  if (error) {
    console.log(error);
  }
  fs.writeFile(pathFile, body, { encoding: 'utf-8' }, function (error) {
    if (error) {
      console.log(error);
    }
  });
});
