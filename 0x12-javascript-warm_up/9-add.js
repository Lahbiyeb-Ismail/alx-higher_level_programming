#!/usr/bin/node

const num1 = process.argv[2];
const num2 = process.argv[3];

function add (a, b) {
  console.log(+a + +b);
}

add(num1, num2);
