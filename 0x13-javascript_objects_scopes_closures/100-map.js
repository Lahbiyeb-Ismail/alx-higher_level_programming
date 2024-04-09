#!/usr/bin/node

const oldList = require('./100-data.js').list;

console.log(oldList);

const newList = oldList.map((item, idx) => item * idx);

console.log(newList);
