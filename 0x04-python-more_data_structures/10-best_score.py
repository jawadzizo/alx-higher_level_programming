#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, (list, set, tuple, dict)):
        return max(a_dictionary)
