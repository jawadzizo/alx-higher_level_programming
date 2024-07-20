#!/usr/bin/node

const arg = Number(process.argv[2]);
const message = arg ? `My number: ${arg}` : 'Not a number';
console.log(message);
