#!/usr/bin/python3
"""lists all the cities in the database, with their state"""

import MySQLdb
import sys


def main():
    """the main function of the module"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    db = MySQLdb.connect("localhost", username, password, database)
    c = db.cursor()
    c.execute("select cities.id, cities.name, states.name \
              FROM cities LEFT JOIN states \
              ON cities.state_id = states.id \
              ORDER BY cities.id;")
    cities = c.fetchall()

    for city in cities:
        print(city)


if __name__ == "__main__":
    main()
