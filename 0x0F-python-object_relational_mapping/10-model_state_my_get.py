#!/usr/bin/python3
"""
This script prints the first State object
from the database `hbtn_0e_6_usa`.
"""
from sys import argv
from model_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    searched_name = argv[4]
    instance = session.query(State).filter(State.name == searched_name).first()
    try:
        print(instance.id)
    except Exception:
        print('Not found')
    session.close()
