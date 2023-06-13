#!/usr/bin/node

/*
 * a script that imports a dictionary of occurrences by user id and computes a dictionary of user ids by occurrence.
 */

const dict = require('./101-data.js').dict;
const newDict = {};

for (const [k, v] of Object.entries(dict)) {
  if (newDict[dict[v]] === undefined) {
    newDict[v] = [k];
  } else {
    newDict[v].push(k);
  }
}
console.log(newDict);
