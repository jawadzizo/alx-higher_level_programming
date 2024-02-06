#!/usr/bin/python3
"""A module that insert a string after the search_string found"""


def append_after(filename="", search_string="", new_string=""):
    """inserts a string after the search_string found"""

    if new_string == "" or search_string == "":
        return

    with open(filename, "r+") as f:
        flist = []
        for line in f:
            flist.append(line)
            if search_string in line:
                flist.append(new_string)

        f.seek(0)
        for element in flist:
            f.write(str(element))
