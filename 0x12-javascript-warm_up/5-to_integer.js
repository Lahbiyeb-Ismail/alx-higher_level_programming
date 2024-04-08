#!/usr/bin/node

const argv = process.argv;

// parseInt(), Number(), and Unary operator (+) function is used in JavaScript.

if (argv.length === 1 || +argv[2] === NaN) {
  console.log('Not a number');
} else {
  console.log(`My number: ${+argv[2]}`);
}
