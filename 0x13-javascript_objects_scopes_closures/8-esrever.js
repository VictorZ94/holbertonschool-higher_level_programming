#!/usr/bin/node
exports.esrever = function (list) {
  const newArray = [];
  while (list.length) {
    newArray.push(list.pop());
  }
  return newArray;
};
