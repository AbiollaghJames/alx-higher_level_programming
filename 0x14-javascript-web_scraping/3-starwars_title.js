#!/usr/bin/node

const request = require('request');
const movieID = process.argv[2];
const requestURL = 'https://swapi-api.alx-tools.com/api/films/movieID';

request(requestURL, function (err, body) {
  if (err) {
    console.error(err);
  }
  console.log(JSON.parse(body.title));
});