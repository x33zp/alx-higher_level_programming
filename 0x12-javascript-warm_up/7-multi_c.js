#!/usr/bin/node
const xValue = process.argv[2]
const textToPrint = 'C is fun'

if (xValue === undefined) {
  console.log('Missing number of occurrences')
} else {
  for (let i = 0; i < xValue; i++) {
    console.log(textToPrint)
  }
}
