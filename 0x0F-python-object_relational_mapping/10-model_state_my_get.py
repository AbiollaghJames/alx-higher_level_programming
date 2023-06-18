#!/usr/bin/python3

"""
 a script that prints the State object with
 the name passed as argument from the
 database hbtn_0e_6_usa
"""


import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from model_state import Base, State


if __name__ = "__main__":
    engine = create_engine(
            'mysql://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )

    Session = sessionmaker(bind=engine)
    session = Session()

    name_searched = sys.argv[4]
    res = session.querry(State).filter_by(name=name_searched).first()

    if res:
        print("{}".format(res.id))
    else:
        print("Not found")

    session.close()
