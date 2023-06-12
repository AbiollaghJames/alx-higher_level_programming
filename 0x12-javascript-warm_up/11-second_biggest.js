#!/usr/bin/node

/*
 * script that searches the second biggest integer in the list of arguments.
 */

const num = process.argv;

if (num.length <= 3) {
  console.log(0);
} else {
  const sort = num.slice(2).sort((a, b) => a - b);
  console.log(sort[sort.length - 2]);
}
