#!/usr/bin/node

module.exports = class Rectangle {
    constructor (w, h) {
        this.width = w;
        this.height = h;

        if (w === undefined || w <= 0 ||
            h === undefined || h <= 0) {
            delete this.width;
            delete this.height;
        }
    }

    print() {
        let row = '';
        for (let i = 0; i < this.width; i++) {
            row += 'X';
        }

        for (let i = 0; i < this.height; i++) {
            console.log(row);
        }
    }
};
