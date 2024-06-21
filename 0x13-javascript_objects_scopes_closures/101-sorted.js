#!/usr/bin/node
const dict = require('./101-data').dict

let sortedDict = {};

for (let key in dict) {
  if (sortedDict[dict[key]] === undefined) {
    sortedDict[dict[key]] = [];
  }
  sortedDict[dict[key]].push(key);
}

console.log(sortedDict)
