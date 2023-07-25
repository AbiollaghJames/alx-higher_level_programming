#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(reqUrl + movieId, function (err, response, body) {
  for (let i = 0; i < JSON.parse(body).characters; i++) {
    request(JSON.parse(body).characters[i], function (err, response, body) {
    console.log(JSON.parse(body).name);
    });
  }
});
