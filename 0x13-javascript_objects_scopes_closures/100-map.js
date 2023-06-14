#!/usr/bin/node
const lst = require('./100-data.js').list;
const lst2 = lst.map((x, i) => x * i);
console.log(lst);
console.log(lst2);
