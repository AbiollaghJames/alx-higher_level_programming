#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/';

request(reqUrl + movieId, function (err, response, body) {
  if (err) {
    throw new Error(err);
  }
  const chars = JSON.parse(body).characters;

  for (let i = 0; i < chars.length; i++) {
    request(chars[i], function (err, response, body) {
      if (err) {
        throw new Error(err);
      }
      console.log(JSON.parse(body).name);
    });
  }
});
