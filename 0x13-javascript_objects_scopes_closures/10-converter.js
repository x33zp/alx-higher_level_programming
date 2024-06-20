#!/usr/bin/node
exports.converter = function (base) {
  return function myConv (number) {
    return number.toString(base);
  };
};
