#!/usr/bin/node

/*
 * script that prints addition of 2  numbers
 */

function add (a, b) {
  return a + b;
}

console.log(add(parseInt(process.argv[2]), parseInt(process.argv[3])));
