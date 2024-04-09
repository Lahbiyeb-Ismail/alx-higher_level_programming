#!/usr/bin/node

const dict = require('./101-data.js').dict;

const newDict = {};

Object.getOwnPropertyNames(dict).forEach((item) => {
  if (newDict[dict[item]] === undefined) {
    newDict[dict[item]] = [item];
  } else newDict[dict[item]].push(item);
});

console.log(newDict);
