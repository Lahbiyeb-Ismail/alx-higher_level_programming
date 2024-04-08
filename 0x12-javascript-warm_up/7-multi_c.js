#!/usr/bin/node

const argv = process.argv;
const message = 'C is fun';

if (+argv[2] === NaN) {
  console.log('Missing number of occurrences');
} else {
  for (let i = 0; i < +argv[2]; i++) {
    console.log(message);
  }
}
