#!/usr/bin/node
// command line arguments
const argumen = process.argv;
if (argumen[2]) {
  console.log(argumen[2]);
} else {
  console.log('No argument');
}
