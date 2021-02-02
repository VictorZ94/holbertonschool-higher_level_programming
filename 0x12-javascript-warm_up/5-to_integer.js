#!/usr/bin/node
// to convert to Int
const argumen = process.argv;
const convertToInt = parseInt(argumen[2]);

if (isNaN(convertToInt)) {
  console.log('Not a number');
} else if (convertToInt === undefined) {
  console.log('Not a number');
} else {
  console.log('My number: ' + convertToInt);
}
