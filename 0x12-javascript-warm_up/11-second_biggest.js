#!/usr/bin/node
const args = process.argv.slice(2);
let secondBiggestInt = 0;

if (args && args.length > 1) {
  sortedArr = args.sort((a, b) => (b - a));
  secondBiggestInt = sortedArr[1];
}

console.log(secondBiggestInt);
