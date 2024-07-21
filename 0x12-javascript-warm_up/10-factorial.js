#!/usr/bin/node

function factorial(number) {
    if (number === undefined || number <= 1) {
        return (1);
    }

    return (factorial(number - 1) * number);
}

console.log(factorial(89));
