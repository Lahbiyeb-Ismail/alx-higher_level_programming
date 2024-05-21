#!/usr/bin/node
// script that prints all characters of a Star Wars movie:

const request = require('request');

const args = process.argv.slice(2);
const filmId = args[0];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

const getCharacterName = (url) => {
  request.get(url, (err, response) => {
    if (err) {
      console.log(err);
    }

    console.log(JSON.parse(response.body).name);
  });
};

const getStarWarsCharacters = () => {
  request.get(apiUrl, (err, response) => {
    if (err) {
      console.log(err);
    }

    const characters = JSON.parse(response.body).characters;
    for (let i = 0; i < characters.length; i++) {
      getCharacterName(characters[i]);
    }
  });
};

getStarWarsCharacters();
