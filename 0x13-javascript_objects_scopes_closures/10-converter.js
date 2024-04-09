#!/usr/bin/node

exports.converter = function (base) {
  function convert (num) {
    return parseInt(num, base);
  }

  return convert;
};
