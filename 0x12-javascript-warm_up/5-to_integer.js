#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 3 || isNaN(argv[2])) {
  console.log('Not a number');
} else {
  console.log(`My number: ${parseInt(argv[2])}`);
}
