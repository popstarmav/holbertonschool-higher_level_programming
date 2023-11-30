#!/usr/bin/node

function createConverter (base) {
  return function convertToBase (num) {
    return num.toString(base);
  };
}

module.exports = { createConverter };
