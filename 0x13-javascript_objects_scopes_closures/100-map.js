#!/usr/bin/node

const list = require('./main').list;
const newList = list.map((element, index) => element * index);

console.log(list);
console.log(newList);
