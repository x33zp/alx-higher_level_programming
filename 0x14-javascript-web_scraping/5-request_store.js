#!/usr/bin/node
const request = require('request');
const fs = require('fs');

const url = process.argv[2];
const file = process.argv[3];

request.get(url, (error, respons, body) => {
  if (error) {
    console.error(error);
  } else {
    fs.writeFile(file, body, err => {
      if (err) {
        console.error(err);
      }
    });
  }
});
