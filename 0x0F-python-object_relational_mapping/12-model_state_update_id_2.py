#!/usr/bin/python3
"""updates the state with the id 2 to 'New Mexico'
"""
import sys
from model_state import State
from sqlalchemy import create_engine, update
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

    session.query(State).filter(State.id == 2).update({"name": "New Mexico"})
    session.commit()


if __name__ == "__main__":
    main()
