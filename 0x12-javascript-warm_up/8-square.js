#!/usr/bin/node

const argv = process.argv;

if (+argv[2]) {
  let square = '';
  for (let i = 0; i < +argv[2]; i++) {
    for (let j = 0; j < +argv[2]; j++) {
      square += 'X';
    }

    if (i < +argv[2] - 1) square += '\n';
  }

  console.log(square);
} else {
  console.log('Missing size');
}
