#!/usr/bin/node
const fs = require('fs');
const filename = process.argv[2];
const textContent = process.argv[3];
fs.writeFile(filename, textContent, 'utf8', function (err) {
  if (err) {
    console.log(err);
  }
});
