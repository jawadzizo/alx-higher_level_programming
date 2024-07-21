#!/usr/bin/node

const args = process.argv;

if (args[2] === undefined || args[3] === undefined) {
    console.log('0');
} else {
    let array = args.slice(2).map((x) => Number(x));
    array = array.sort((a, b) => b - a);
    console.log(array[1]);
}
