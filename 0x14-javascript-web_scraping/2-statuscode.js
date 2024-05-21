#!/usr/bin/node
// script that display the status code of a GET request.

const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

const getStatusCode = () => {
  request.get(url, (err, response) => {
    if (err) {
      console.log(err);
    }
    console.log('code: ', response.statusCode);
  });
};

getStatusCode();
