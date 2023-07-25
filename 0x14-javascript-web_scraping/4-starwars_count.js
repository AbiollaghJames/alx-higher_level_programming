#!/usr/bin/node

const request = require('request');
const API_URL = process.argv[2];

request(API_URL, function (error, response, body) {
  if (error) {
    throw new Error(error);
  }
  const num = JSON.parse(body).results.filter((element) => {
    return element.characters.filter((url) => {
      return url.includes('18'); }).length;
  }).length;
  console.log(num);
});