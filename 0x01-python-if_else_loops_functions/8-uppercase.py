#!/usr/bin/python3

def uppercase(str):
    for i in range(len(str)):
        if ord(str[i]) >= 97 and ord(str[i]) <= 122:
            print("{}{}" .format(chr(ord(str[i]) - 32), "\n" if i == (len(str) - 1) else ""), end="")
        else:
            print("{}{}" .format(str[i], "\n" if i == (len(str) - 1) else ""), end="")
