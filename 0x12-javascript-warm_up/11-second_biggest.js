#!/usr/bin/node

const argv = process.argv;

function second_biggest (arr) {
  if (!arr || arr.length === 1) {
    console.log('0');
  } else {
    arr.sort((a, b) => b - a);
    console.log(arr[1]);
  }
}

second_biggest(argv.slice(2));
