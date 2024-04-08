#!/usr/bin/node

const args = process.args;

if (!args) {
  console.log('No argument');
} else {
  console.log('Argument found');
}
