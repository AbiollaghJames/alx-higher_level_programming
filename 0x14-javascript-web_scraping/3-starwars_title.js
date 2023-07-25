#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const requestUrl = 'https://swapi-api.alx-tools.com/api/films/${movieId}';

request(requestUrl, function (error, response, body) {
  if (error) {
    throw new Error(error);
  }
  if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    return;
  }
});