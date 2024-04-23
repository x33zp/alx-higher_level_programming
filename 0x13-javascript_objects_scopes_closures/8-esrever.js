#!/usr/bin/node
exports.esrever = function (list) {
  reversedList = []
  for (let i = 0; i < list.length; i++) {
    reversedList.unshift(list[i])
  }
  return reversedList
};
