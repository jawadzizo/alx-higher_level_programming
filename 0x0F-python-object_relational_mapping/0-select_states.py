#!/usr/bin/python3
"""lists all states in the given database"""

import MySQLdb
import sys


def main():
    """the main function of the module"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, database)
    c = db.cursor()
    c.execute("SELECT * FROM states ORDER BY id;")
    states = c.fetchall()

    for state in states:
        print(state)


if __name__ == "__main__":
    main()
