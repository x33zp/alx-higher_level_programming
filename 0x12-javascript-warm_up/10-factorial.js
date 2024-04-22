#!/usr/bin/node
const { argv } = require('node:process');

factorial = (n) => {
  return isNaN(n) || n === 0 ? 1 : n * factorial(n - 1);
}

console.log(factorial(Number(argv[2])));
