#!/usr/bin/node

const argv = process.argv;

if (argv[1] && !argv[2]) {
  console.log('No argument');
}

console.log(argv[2]);
