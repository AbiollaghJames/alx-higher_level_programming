#!/usr/bin/python3

"""
a script that prints all City objects
from the database hbtn_0e_14_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )
    Session = sessionmaker(bind=engine)
    session = Session()

    res = session.query(City, State).filter(City.state_id == State.id)\
        .order_by(City.id).all()

    for c, s in res:
        print("{}: ({}) {}".format(s.name, c.id, c.name))

    session.close()
