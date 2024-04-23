#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let count = 0;
  list.forEach(item =>
    searchElement === item ? count++ : null
  );
  return count;
};
