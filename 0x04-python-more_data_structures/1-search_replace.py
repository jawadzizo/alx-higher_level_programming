#!/usr/bin/python3

def search_replace(my_list, search, replace):
    new = list(map(lambda x: replace if search == x else x, my_list))
    return new
