#!/usr/bin/node
exports.esrever = function (list) {
  const revsList = [];

  list.forEach(item => {
    revsList.unshift(item);
  });

  return revsList;
};
