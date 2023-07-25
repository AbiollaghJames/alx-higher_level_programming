#!/usr/bin/node

const request = require('request');
const movieId = process.argv[2];
const reqUrl = 'https://swapi-api.alx-tools.com/api/films/';
let chars = [];

request(reqUrl + movieId, function (err, response, body) {
  if (err) {
    throw new Error(err);
  }
  const body = JSON.parse(body);
  chars = body.characters;
  captureChar(0);
});

const captureChar = (i) => {
  if (i === chars.length) {
    return;
  }
  request(chars[i], function (err, response, body) {
    if (err) {
      throw new Error(err);
    }
    const charsData = JSON.parse(body);
    console.log(charsData.name);
    captureChar(i + 1);
  });
};

