#!/usr/bin/python3

def print_last_digit(number):
    if number >= 0:
        print(f"{number % 10}")
    else:
        number = -number
        print(f"{number % 10}")

    return number % 10
