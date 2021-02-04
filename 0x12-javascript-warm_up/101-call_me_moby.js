#!/usr/bin/node
exports.callMeMoby = function (x, theFunction) {
  if (x > 0) {
    while (x--) {
      theFunction();
    }
  }
};
