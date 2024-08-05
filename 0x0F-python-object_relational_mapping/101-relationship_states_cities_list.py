#!/usr/bin/python3
"""lists the states with the cities in them
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

    states = session.query(State)

    for state in states:
        print(f"{state.id}: {state.name}")

        for city in state.cities:
            print(f"    {city.id}: {city.name}")


if __name__ == "__main__":
    main()
