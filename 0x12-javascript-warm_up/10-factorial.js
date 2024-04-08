#!/usr/bin/node

const argv = process.argv;

function factorial(n) {
  if (!n || n === 1 || typeof n === NaN) return 1;

  return n * factorial(n - 1);
}

console.log(factorial(+argv[2]));
