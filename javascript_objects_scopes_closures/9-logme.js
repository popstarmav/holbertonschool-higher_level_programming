#!/usr/bin/node

let narg = 0;

function logMe (item) {
  console.log(`${narg}: ${item}`);
  narg++;
}

module.exports = { logMe };
