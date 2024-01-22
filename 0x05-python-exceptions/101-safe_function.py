#!/usr/bin/python3
import os


def safe_function(fct, *args):

    try:
        result = fct(*args)
        return (result)

    except Exception as er:
        text = "Exception: " + str(er) + '\n'
        os.write(2, text.encode("UTF-8"))
        return
