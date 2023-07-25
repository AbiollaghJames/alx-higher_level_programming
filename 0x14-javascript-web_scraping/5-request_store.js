#!/usr/bin/node

const request = require('request');
const fs = require('fs');

const requestUrl = process.argv[2];
const filePath = process.argv[3];

request(requestUrl, function (error, response, body) {
  if (error) {
    throw new Error(error);
  } else if (response.statusCode === 200) {
    fs.writeFile(filePath, body, 'utf-8', (err, data) => {
      if (err) {
        throw new Error(err);
      }
    });
  } else {
    console.log(response.statusCode);
  }
});
