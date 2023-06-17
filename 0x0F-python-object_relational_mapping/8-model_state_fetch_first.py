#!/usr/bin/python3

"""
a script that lists all State objects from the database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
        'mysql+mysqldb://{}:{}@localhost/{}'.format(
            sys.argv[1], sys.argv[2], sys.argv[3]
            )
        )
    Session = sessionmaker(bind=engine)
    session = Session()

    f_row = session.query(State).first()
    if f_row:
        print("{}: {}".format(f_row.id, f_row.name))
    else:
        print("")
    session.close()
