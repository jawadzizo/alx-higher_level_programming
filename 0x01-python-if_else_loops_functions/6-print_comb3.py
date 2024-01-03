#!/usr/bin/python3

for i in range(9):
    for j in range(1, 10):
        if j > i:
            print("{}{}" .format(i, j), end="")
            print("{}" .format("\n" if i == 8 and j == 9 else ", "), end="")
