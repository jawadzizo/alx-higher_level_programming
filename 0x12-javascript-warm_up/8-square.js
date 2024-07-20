#!/usr/bin/node

const arg = Number(process.argv[2]);
if (!arg) {
    console.log('Missing size');
}

else {
    let square = [];
    for (let i = 0; i < arg; i++) {
        square.push('X');
    }

    square = square.join('');

    for (let i = 0; i < arg; i++) {
        console.log(square);
    }
}
