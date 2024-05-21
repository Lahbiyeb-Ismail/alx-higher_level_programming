#!/usr/bin/node
// script that prints all characters of a Star Wars movie:

const request = require('request');

const args = process.argv.slice(2);
const filmId = args[0];

const apiUrl = `https://swapi-api.alx-tools.com/api/films/${filmId}`;

const getStarWarsCharacters = () => {
  request.get(apiUrl, (err, response) => {
    if (err) {
      console.log(err);
      return;
    }

    const characters = JSON.parse(response.body).characters;

    const printCharacterName = (url) => {
      return new Promise((resolve, reject) => {
        request.get(url, (err, response) => {
          if (err) {
            reject(err);
          } else {
            resolve(JSON.parse(response.body).name);
          }
        });
      });
    };

    const fetchAndPrintCharacters = async () => {
      for (let i = 0; i < characters.length; i++) {
        try {
          const name = await printCharacterName(characters[i]);
          console.log(name);
        } catch (error) {
          console.log(error);
        }
      }
    };

    fetchAndPrintCharacters();
  });
};

getStarWarsCharacters();
