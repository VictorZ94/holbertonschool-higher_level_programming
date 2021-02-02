#!/usr/bin/node
// to print using while loop by my choice
let number = parseInt(process.argv[2]);
if (isNaN(number) || number === undefined) {
  console.log('Missing number of occurrences');
} else {
  if (number > 0) {
    while (number--) {
      console.log('C is fun');
    }
  }
}
