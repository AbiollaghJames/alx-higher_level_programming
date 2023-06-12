#!/usr/bin/node

/*
 * script that searches the second biggest integer in the list of arguments.
 */

if (process.argv.length <= 3) {
  console.log('0');
} else {
  const numbers = process.argv.sort();
  console.log(numbers.reverse()[1]);
}
