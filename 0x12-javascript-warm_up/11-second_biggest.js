#!/usr/bin/node
const args = process.argv.slice(2);
let sortedArgs;

if (args === undefined || args.length < 2) {
  console.log(0);
} else {
  sortedArgs = args.sort();
}

console.log(sortedArgs[sortedArgs.length - 2]);
