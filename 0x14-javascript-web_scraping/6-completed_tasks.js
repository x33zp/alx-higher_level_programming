#!/usr/bin/node
const request = require('request')

const url = process.argv[2]

request.get(url, (error, response, body) => {
  if (error) {
    console.error(error)
  } else {
    const results = JSON.parse(body);
    const obj = {}
    results.forEach(result => {
        if (result.completed) {
	  if (obj[result.userId]) {
            obj[result.userId]++
	  } else {
            obj[result.userId] = 1;
	  }
	}
    });

    console.log(obj)
  }
});
