#!/usr/bin/node
// script that prints the title of a Star Wars movie where the episode number matches a given integer.

const request = require('request');

const args = process.argv.slice(2);
const fileId = args[0];
const url = `https://swapi-api.hbtn.io/api/films/${fileId}`;

const getStarWarsTitle = () => {
  request.get(url, (err, response) => {
    if (err) {
      console.log(err);
    }
    console.log(JSON.parse(response.body).title);
  });
};

getStarWarsTitle();
