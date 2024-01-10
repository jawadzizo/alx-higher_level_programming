#!/usr/bin/python3

def best_score(a_dictionary):
    if isinstance(a_dictionary, (dict)) and len(a_dictionary):
        max_key = ""
        max_value = ""
        for k, v in a_dictionary.items():
            if isinstance(max_value, str):
                max_value = v
            if v > max_value:
                max_value = v
                max_key = k

        return max_key
