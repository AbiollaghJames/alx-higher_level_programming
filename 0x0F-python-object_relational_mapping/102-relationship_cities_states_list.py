#!/usr/bin/python3

"""
a script that lists all City objects
from the database hbtn_0e_101_usa
"""
import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from relationship_state import Base, State
from relationship_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'.format
                           (sys.argv[1], sys.argv[2], sys.argv[3]))

    Session = sessionmaker(bind=engine)
    session = Session()
    results = session.query(State).all()
    for res in results:
        for c in state.cities:
            print("{}: {} -> {}".format(c.id, c.name, res.name))
    session.close()
