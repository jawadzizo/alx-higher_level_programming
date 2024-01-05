#!/usr/bin/python3

def add_tuple(tuple_a=(), tuple_b=()):
    new_tuple = ()

    tuple_a = tuple_a + (0, 0)
    tuple_b = tuple_b + (0, 0)

    for i in range(2):
        a = tuple_a[i] + tuple_b[i]
        new_tuple = new_tuple + (a,)

    return new_tuple
