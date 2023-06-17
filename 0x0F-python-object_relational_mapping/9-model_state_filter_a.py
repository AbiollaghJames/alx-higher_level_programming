#!/usr/bin/python3

"""
 a script that lists all State objects that contain the letter a from the database hbtn_0e_6_usa
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

    names = session.query(State).order_by(State.id).all()
    new_names = []

    for name in names:
        new_names.append(name)

        for letter in new_names:
            if 'a' in letter:
                print(letter)
    session.close()
