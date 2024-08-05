#!/usr/bin/python3
"""lists the state being searched for"""

import MySQLdb
import sys


def main():
    """the main function of the module"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]
    searched_state = sys.argv[4]

    db = MySQLdb.connect("localhost", username, password, database)
    c = db.cursor()
    c.execute("SELECT * FROM states WHERE name = '{}' ORDER BY id;"
              .format(searched_state))
    states = [state for state in c.fetchall() if state[1] == searched_state]

    for state in states:
        print(state)


if __name__ == "__main__":
    main()
