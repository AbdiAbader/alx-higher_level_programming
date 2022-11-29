#!/usr/bin/node

exports.nbOccurences = function (list, searchElement) {
  const occurence = list.filter(n => n === searchElement);
  return occurence.length;
};
