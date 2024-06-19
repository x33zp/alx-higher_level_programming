#!/usr/bin/node
const args = process.argv.slice(2);
let secondBiggestInt = 0;

if (args && args.length > 1) {
  args.sort((a, b) => (b - a));
  secondBiggestInt = args[1];
}

console.log(secondBiggestInt);
