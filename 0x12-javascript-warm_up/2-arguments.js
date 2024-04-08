#!/usr/bin/node

const args = process.args;
let message;

args.length > 0 ? (message = 'Argument found') : (message = 'No argument');

console.log(message);
