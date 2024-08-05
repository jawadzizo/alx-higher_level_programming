#!/usr/bin/python3
"""lists the cities with their state
"""
import sys
from relationship_state import State, Base
from relationship_city import City
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

    cities = session.query(City).order_by(City.id)

    for city in cities:
        print(f"{city.id}: {city.name} -> {city.state.name}")


if __name__ == "__main__":
    main()
