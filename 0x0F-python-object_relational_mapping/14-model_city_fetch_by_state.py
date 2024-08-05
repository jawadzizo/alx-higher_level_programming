#!/usr/bin/python3
"""lists all cities in the database with their state and id
"""
import sys
from model_state import State
from model_city import City
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


def main():
    """the main function of the module"""
    username = sys.argv[1]
    password = sys.argv[2]
    database = sys.argv[3]

    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(username, password, database))
    Session = sessionmaker(bind=engine)
    session = Session()

    cities = session.query(State.name, City.id, City.name).join(City) \
        .order_by(City.id)

    for city in cities:
        print(f"{city[0]}: ({city[1]}) {city[2]}")


if __name__ == "__main__":
    main()
