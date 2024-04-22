#!/usr/bin/node
const { argv } = require('node:process');

if (argv.length < 3 || isNaN(argv[2])) {
  console.log('Missing size');
} else {
  for (let i = 0; i < argv[2]; i++) {
    console.log('X'.repeat(argv[2]));
  }
}
