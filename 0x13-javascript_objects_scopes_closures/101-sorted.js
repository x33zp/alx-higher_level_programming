#!/usr/bin/node
const { dict } = require('./101-data');

const occurrenceDict = {};

for (const key in dict) {
  const value = dict[key];

  if (!(value in occurrenceDict)) {
    occurrenceDict[value] = [];
  }

  occurrenceDict[value].push(key);
}

console.log(occurrenceDict);
