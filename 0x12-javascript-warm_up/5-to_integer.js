#!/usr/bin/node

/*
 * print something if 1st arg can be converted to an int
 */

const num = Math.floor(Number(process.argv[2]));

if (!isNaN(num) && Number.isInteger(num)) {
  console.log('My number: ', num);
} else {
  console.log('Not a number');
}
