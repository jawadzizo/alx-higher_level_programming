#!/usr/bin/python3
"""lists all the cities in the selected state"""

import MySQLdb
import sys


def main():
    """the main function of the module"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, database)
    c = db.cursor()
    c.execute("select cities.name \
              FROM cities JOIN states \
              ON cities.state_id = states.id \
              WHERE states.name='{}' \
              ORDER BY cities.id;"
              .format(sys.argv[4]))
    cities = ", ".join([city[0] for city in c.fetchall()])

    print(cities)


if __name__ == "__main__":
    main()
