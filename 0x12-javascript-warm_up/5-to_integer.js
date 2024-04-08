#!/usr/bin/node

const argv = process.argv;

// parseInt(), Number(), and Unary operator (+) function is used in JavaScript.

if (+argv[2]) {
  console.log(`My number: ${+argv[2]}`);
} else {
  console.log('Not a number');
}
