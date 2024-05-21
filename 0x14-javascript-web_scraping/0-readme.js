#!/usr/bin/node
// script that reads and prints the content of a file.

const fs = require('fs');
const args = process.argv.slice(2);

const filename = args[0];

const readAndPrint = () => {
  fs.readFile(filename, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
      return;
    }
    console.log(data);
  });
};

readAndPrint();
