#!/usr/bin/node
// get started with function recursively
const n = parseInt(process.argv[2]);
// console.log(typeof(n));
console.log(factorial(n));
function factorial (n) {
  if (isNaN(n)) {
    return (1);
  }

  if (n < 1) {
    return (1);
  }
  return (n * factorial(n - 1));
}
