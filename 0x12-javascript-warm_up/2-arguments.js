#!/usr/bin/node
// command line arguments
const argumen = process.argv.length;
if (argumen >= 4) {
  console.log('Arguments found');
} else if (argumen === 3) {
  console.log('Argument found');
} else {
  console.log('No argument');
}
