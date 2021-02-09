#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let i = 0;
  list.forEach(iter);
  function iter (item, index) {
    if (item === searchElement) {
      i++;
    }
  }
  return (i);
};
