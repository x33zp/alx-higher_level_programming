#!/usr/bin/node
const request = require('request');

const id = process.argv[2];
const url = 'https://swapi-api.alx-tools.com/api/films/';
request.get(`${url}${id}`, (error, response, body) => {
  if (error) {
    console.error(error);
  } else {
    console.log(JSON.parse(body).title);
  }
});
