#!/usr/bin/node
// script that gets the contents of a webpage and stores it in a file.

const request = require('request');
const fs = require('fs');

const args = process.argv.slice(2);
const url = args[0];
const filename = args[1];

const requestStore = () => {
  request.get(url, (err, response) => {
    if (err) {
      console.log(err);
    }

    const fileContent = response.body;

    fs.writeFile(filename, fileContent, 'utf8', (err) => {
      if (err) {
        console.log(err);
      }
    });
  });
};

requestStore();
