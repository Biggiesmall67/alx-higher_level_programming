#!/usr/bin/node

exports.esrever = function (list) {
  const lst = [];
  for (let i = list.length - 1; i >= 0; i--) {
    lst.push(list[i]);
  }
  return (lst);
};
