#!/usr/bin/node
const args = process.argv.slice(2);

if (args === undefined || args.length < 2) {
  console.log(0);
} else {
  const sortedArgs = args.sort();
  console.log(sortedArgs[sortedArgs.length - 2]);
}
