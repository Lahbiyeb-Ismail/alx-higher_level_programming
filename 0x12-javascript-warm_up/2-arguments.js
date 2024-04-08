#!/usr/bin/node

const args = process.args;
let message;

if (!args) {
  message = 'No argument';
} else if (args.length === 1) {
  message = 'Argument found';
} else {
  message = 'Arguments found';
}

console.log(message);
