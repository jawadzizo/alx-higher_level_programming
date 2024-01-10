#!/usr/bin/python3

def multiply_by_2(a_dictionary):
    new = {k: v*2 for k, v in a_dictionary.items() if isinstance(v, int)}
    return new
