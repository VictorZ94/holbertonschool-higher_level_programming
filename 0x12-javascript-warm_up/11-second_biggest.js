#!/usr/bin/node
// get started with function recursively
const argumen = process.argv;
// console.log(argumen);
console.log(secBiggest(argumen));
function secBiggest (argumen) {
  if (argumen.length <= 3) {
    return 0;
  }

  const myArray = new Array([]);
  let j = 0;
  for (let i = 2; i < argumen.length; i++) {
    myArray[j] = parseInt(argumen[i]);
    j++;
  }
  const sortedArray = myArray.sort(function (a, b) { return a - b; });
  return (sortedArray[j - 2]);
}
