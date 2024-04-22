#!/usr/bin/node
const { argv } = require('node:process');

const factorial = (n) => {
  return isNaN(n) || n <= 1 ? 1 : n * factorial(n - 1);
};

console.log(factorial(argv[2]));
