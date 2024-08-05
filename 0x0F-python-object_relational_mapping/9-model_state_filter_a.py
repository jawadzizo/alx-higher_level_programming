#!/usr/bin/python3
"""lists the first state in the database using states.id
"""
import sys
from model_state import State
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

    states = session.query(State).filter(State.name.contains('a')) \
        .order_by(State.id)
    for state in states:
        print(f"{state.id}: {state.name}")


if __name__ == "__main__":
    main()
