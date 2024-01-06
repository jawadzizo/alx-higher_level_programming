#!/usr/bin/python3

def divisible_by_2(my_list=[]):

    if len(my_list) == 0:
        return

    is_divisible = []

    for element in my_list:
        if element % 2 == 0:
            is_divisible.append(True)
        else:
            is_divisible.append(False)

    return is_divisible
