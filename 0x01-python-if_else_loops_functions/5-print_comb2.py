#!/usr/bin/python3

for x in range(0, 100):
    print("{:02}{}" .format(x, ", " if x != 99 else "\n"), end="")
