#!/usr/bin/node
const direc = require('./101-data.js').dict;
const ndix = {};

for (const k in direc) {
  if (direc[k] in ndix) {
    ndix[direc[k]].push(k);
  } else {
    ndix[direc[k]] = [k];
  }
}
console.log(ndix);
