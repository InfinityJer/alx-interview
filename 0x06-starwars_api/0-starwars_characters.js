#!/usr/bin/node

const request = require('request');

const movieId = process.argv[2];

if (!movieId || isNaN(movieId)) {
  console.error('Please provide a valid movie ID');
  process.exit(1);
}

const API_URL = `https://swapi-api.hbtn.io/api`;

const url = `${API_URL}/films/${movieId}/`;

function fetchCharacterName(characterUrl) {
  return new Promise((resolve, reject) => {
    request(characterUrl, (error, response, body) => {
      if (error) {
        reject(error);
        return;
      }

      if (response.statusCode !== 200) {
        reject(`Invalid response: ${response.statusCode}`);
        return;
      }

      const character = JSON.parse(body);
      resolve(character.name);
    });
  });
}

request(url, (error, response, body) => {
  if (error) {
    console.error('Error:', error);
    process.exit(1);
  }

  if (response.statusCode !== 200) {
    console.error('Invalid response:', response.statusCode);
    process.exit(1);
  }

  const film = JSON.parse(body);
  const characters = film.characters;

  const characterPromises = characters.map(fetchCharacterName);

  Promise.all(characterPromises)
    .then(names => names.forEach(name => console.log(name)))
    .catch(err => {
      console.error('Error:', err);
      process.exit(1);
    });
});
