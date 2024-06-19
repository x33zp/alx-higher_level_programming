#!/usr/bin/node
const xValue = parseInt(process.argv[2]);

if (xValue === undefined || isNaN(xValue)) {
  console.log('Missing size');
} else {
  for (let i = 0; i < xValue; i++) {
    console.log('X'.repeat(xValue));
  }
}
