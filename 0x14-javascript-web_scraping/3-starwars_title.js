#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films/${movieID}';

request(requestURL, function(err, response, body) {
  if (err) {
    throw new Error(err);
  }

  if (response.statusCode !== 200) {
    return;
  }
  const filmData = JSON.parse(body);
  console.log(filmData.title);
});