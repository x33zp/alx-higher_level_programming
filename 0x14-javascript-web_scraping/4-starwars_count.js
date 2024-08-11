#!/usr/bin/node
const request = require('request');

const url = process.argv[2];
let count = 0;

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    const results = JSON.parse(body).results;
    results.forEach(result => {
      result.characters.forEach(char => {
        if (char.includes('18')) {
          count++;
        }
      });
    });
    console.log(count);
  }
});
