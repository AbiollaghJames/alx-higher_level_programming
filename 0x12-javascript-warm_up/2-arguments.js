#!/usr/bin/node

/*
 * print message depending on command-line-args
 */

if (process.argv.length <= 2) {
  console.log('No argument');
} else if (process.argv.length <= 3) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
