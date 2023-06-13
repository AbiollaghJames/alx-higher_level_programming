#!/usr/bin/node

/*
 * a script that imports an array and computes a new array
 */

const list = require('./100-data.js').list;
const newArray = list.map((value, i) => {
  return value * i;
});
console.log(list);
console.log(newArray);
