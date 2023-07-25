#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(reqUrl + movieId, function (err, response, body) {
  const chars = JSON.parse(body).characters;
  
  for (let i = 0; i < chars.length; i++) {
    request(chars[i], function (err, response, body) {
      console.log(JSON.parse(body).name);
    });
  }
});
