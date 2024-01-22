#!/usr/bin/python3
import os


def safe_print_integer_err(value):
    try:
        print("{:d}".format(value))
        return (True)

    except Exception as er:
        text = "Exception: " + str(er) + '\n'
        os.write(2, text.encode("UTF-8"))
        return (False)
