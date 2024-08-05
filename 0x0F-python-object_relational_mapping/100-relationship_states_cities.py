#!/usr/bin/python3
"""creates a new state 'California' and inside it the city 'San Francisco'
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

    Base.metadata.create_all(engine)

    c = State(name="California", cities=[City(name="San Francisco")])
    session.add(c)
    session.commit()


if __name__ == "__main__":
    main()
