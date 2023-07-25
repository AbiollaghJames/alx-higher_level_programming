#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const REQ_URL = 'https://swapi-api.alx-tools.com/api/films/';

request(REQ_URL + movieId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(response.statusCode);
  }
});