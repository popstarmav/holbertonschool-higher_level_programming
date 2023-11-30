#!/usr/bin/node

function nbOccurences(list, searchElement) {
  let nOccurrences = 0;
  for (let element of list) {
    if (searchElement === element) {
      nOccurrences++;
    }
  }
  return nOccurrences;
}

module.exports = { nbOccurences };
