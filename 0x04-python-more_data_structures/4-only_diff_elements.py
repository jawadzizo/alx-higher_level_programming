#!/usr/bin/python3

def only_diff_elements(set_1, set_2):
    result1 = list(filter(lambda x: x not in set_2, set_1))
    result2 = list(filter(lambda x: x not in set_1, set_2))
    return result1 + result2
