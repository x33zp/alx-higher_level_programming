#!/usr/bin/node
const { argv } = require('node:process');

function add (a, b) {
  return Math.floor(a) + Math.floor(b);
}

console.log(add(argv[2], argv[3]));
