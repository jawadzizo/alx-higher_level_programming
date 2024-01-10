#!/usr/bin/python3
def complex_delete(a_dictionary, value):
    if isinstance(a_dictionary, dict):
        another_dictionary = a_dictionary.copy()
        for k, v in another_dictionary.items():
            if v == value:
                del a_dictionary[k]

    return a_dictionary
