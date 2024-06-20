#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let occur = 0;

  list.forEach(item => {
    if (item === searchElement) {
      occur += 1;
    }
  });

  return occur;
};
