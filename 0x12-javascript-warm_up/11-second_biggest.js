#!/usr/bin/node
const { argv } = require('node:process');

const arg = argv.slice(2);
arg.sort((a, b) => a - b);
console.log(arg.length < 2 ? 0 : arg[arg.length - 2]);
