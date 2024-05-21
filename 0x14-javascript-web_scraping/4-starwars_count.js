#!/usr/bin/node
// script that prints the number of movies where the character “Wedge Antilles” is present.

const request = require('request');

const args = process.argv.slice(2);
const url = args[0];

const getStarWarsCount = () => {
  request.get(url, (err, response) => {
    if (err) {
      console.log(err);
    }

    const results = JSON.parse(response.body).results;
    let numOfMovies = 0;

    for (let i = 0; i < results.length; i++) {
      const characters = results[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j].includes('18')) {
          numOfMovies++;
        }
      }
    }

    console.log(numOfMovies);
  });
};

getStarWarsCount();
