#!/usr/bin/python3

def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0

    nom = 0
    denom = 0

    for tpl in my_list:
        x, y = tpl
        nom += (x * y)
        denom += y

    return nom / denom
