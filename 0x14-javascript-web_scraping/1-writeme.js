#!/usr/bin/node
// script that writes a string to a file.

const fs = require('fs');
const args = process.argv.slice(2);

const filename = args[0];
const fileContent = args[1];

const writeme = () => {
  fs.writeFile(filename, fileContent, 'utf8', (err, data) => {
    if (err) {
      console.log(err);
    }
  });
};

writeme();
