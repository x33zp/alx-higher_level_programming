#!/usr/bin/node
const dict = require('./101-data').dict;

const sortedDict = {};

for (const key in dict) {
  if (sortedDict[dict[key]] === undefined) {
    sortedDict[dict[key]] = [];
  }
  sortedDict[dict[key]].push(key);
}

console.log(sortedDict);
