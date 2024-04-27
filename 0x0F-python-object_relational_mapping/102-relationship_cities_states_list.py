#!/usr/bin/python3
"""
lists all City objects from the database
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

    cities_and_states = session.query(City, State).join(State)

    for city, state in cities_and_states:
        print('{}: {} -> {}'.format(city.id, city.name, state.name))

    session.close()
