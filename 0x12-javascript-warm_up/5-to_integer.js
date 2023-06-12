#!/usr/bin/node

/*
 * print something if 1st arg can be converted to an int
 */

if (isNaN(process.argv[2])) {
  console.log('Not a number');
} else {
  console.log('My number: ' + parseInt(process.argv[2]));
}
