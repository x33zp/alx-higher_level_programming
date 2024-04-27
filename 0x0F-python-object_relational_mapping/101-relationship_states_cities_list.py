#!/usr/bin/python3
"""
Lists all State objects and corresponding
City objects contained in the DB
"""
from sys import argv
from relationship_city import City
from relationship_state import Base, State
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == '__main__':
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(argv[1], argv[2], argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()

    states = session.query(State)

    for state in states:
        print('{}: {}'.format(state.id, state.name))
        cities = state.cities
        for city in cities:
            print('{:>5}: {}'.format(city.id, city.name))

    session.close()
