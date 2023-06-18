#!/usr/bin/python3
"""
create clifornia state and san fransico city
"""


import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from relationship_city import City
from relationship_state import State, Base


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.rgv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()
    new_s = State(name='California')
    new_c = City(name='San Francisco')
    new_s.cities.append(new_c)
    session.add(new_s)
    session.commit()
    session.close()
