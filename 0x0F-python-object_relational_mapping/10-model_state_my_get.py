#!/usr/bin/python3

"""
a script that prints the State object
with the name passed as argument
from the database hbtn_0e_6_usa
"""

import sys
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from model_state import Base, State


if __name__ == "__main__":
    engine = create_engine(
            'mysql+mysqldb://{}:{}@localhost/{}'.format(
                sys.argv[1], sys.argv[2], sys.argv[3]
                )
            )

    Session = sessionmaker(bind=engine)
    session = Sesion()

    res = session.query(State).filter_by(name=sys.argv[4]).first()

    if res:
        print("{}".format(res.id))
    else:
        print("Not found")

    session.close()
