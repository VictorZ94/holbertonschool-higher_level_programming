#!/usr/bin/node
// to print using size * size
const number = parseInt(process.argv[2]);
if (isNaN(number) || number === undefined) {
  console.log('Missing size');
}
if (number > 0) {
  for (let size = 0; size < number; size++) {
    console.log('X'.repeat(number));
  }
}
