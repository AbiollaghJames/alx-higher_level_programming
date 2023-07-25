#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/' + movieId;

function getRequest (array, i) {
  if (i === array) {
    return;
  }
  request(array[i], function (err, response, body) {
    if (err) {
      throw new Error(err);
    }
    console.log(JSON.parse(body).name);
    getRequest(array, i + 1);
  });
}
request(reqUrl, function (err, response, body) {
  if (err) {
    throw new Error(err);
  }
  const chars = JSON.parse(body).characters;
  getRequest(chars, 0);
});
