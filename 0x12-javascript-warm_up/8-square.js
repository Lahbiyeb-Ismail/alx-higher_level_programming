#!/usr/bin/node

const argv = process.argv;

if (+argv[2]) {
  for (let i = 0; i < +argv[2]; i++) {
    for (let j = 0; j < +argv[2]; j++) console.log('#');
  }
} else {
  console.log('Missing size');
}
