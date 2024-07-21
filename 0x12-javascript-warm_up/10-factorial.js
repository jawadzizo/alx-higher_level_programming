#!/usr/bin/node

function factorial(number) {
    if (Number.isNaN(number) || number <= 1) {
        return (1);
    }

    return (factorial(number - 1) * number);
}

const arg = Number(process.argv[2]);

console.log(factorial(arg));
