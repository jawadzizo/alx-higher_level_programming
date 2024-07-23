#!/usr/bin/node
const SquareTemp = require('./5-square');

module.exports = class Square extends SquareTemp {

    charPrint(c) {
        const letter = (c !== undefined) ? c : 'X';
        for (let i = 0; i < this.width; i++) {
            console.log(letter.repeat(this.width));
        }
    }
};
