#!/usr/bin/node
const { argv } = require('node:process');
const fs = require('fs');

const arg1 = argv[2];
const arg2 = argv[3];
const arg3 = argv[4];

const text1 = fs.readFileSync(arg1, 'utf8');
const text2 = fs.readFileSync(arg2, 'utf8');
fs.writeFileSync(arg3, text1 + text2);
