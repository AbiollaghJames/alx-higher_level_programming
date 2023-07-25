#!/usr/bin/node

const request = require('request');
const epId = process.argv[2];
const REQ_URL = 'https://swapi-api.hbtn.io/api/films/';

request(REQ_URL + epId, function (error, response, body) {
  if (error) {
    console.log(error);
  } else if (response.statusCode === 200) {
    console.log(JSON.parse(body).title);
  } else {
    console.log(response.statusCode);
  }
});