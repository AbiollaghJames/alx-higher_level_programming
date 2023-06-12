#!/usr/bin/node

/*
 * print something if 1st arg can be converted to an int
 */

if (!isNaN(process.argv[2]) && Number.isInteger(Number(process.argv[2]))) {
	console.log('My number: ', process.argv[2]);
} else {
	console.log('Not a number');
}
