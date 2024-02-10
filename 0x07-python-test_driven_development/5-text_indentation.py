#!/usr/bin/python3
"""
A module for printing a text with 2 new lines after either . : ?
text must be string
atleast 1 argument should be passed
return nothing
"""


def text_indentation(text):
    """
    prints a text with 2 new lines after each of these characters: ., ? and :
    """

    if isinstance(text, str) is False:
        raise TypeError("text must be a string")

    char = ['.', ':', "?"]
    print_space = True

    for i in range(len(text)):
        if text[i] == " " and print_space is False:
            continue

        print(text[i], end="")
        print_space = True

        if text[i] in char:
            print("\n")
            print_space = False
