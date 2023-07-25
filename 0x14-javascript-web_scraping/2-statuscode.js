#!/usr/bin/node

const request = require('request');
const requestURL = process.argv[2];

request(requestURL, function (err, response) {
  if (err) {
    console.error(err);
  } else {
    console.log('code:', response.statusCode);
  }
});
