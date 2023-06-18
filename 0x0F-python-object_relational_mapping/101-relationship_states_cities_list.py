#!/usr/bin/python3

"""
 a script that lists all State objects
 and corresponding City objects,
 contained in the database hbtn_0e_101_usa
 """

 import sys
 from sqlalchemy import create_engine
 from sqlalchemy.orm import sessionmaker
 from relationship_state import Base, State
 from relationship_city import City


 if __name__ == "__main__":
     engine = create_engine(
             'mysql+mysqldb://{}:{}@localhost/{}'.format(
                 sys.argv[1], sys.argv[2], sys.argv[3]
                 )
             )

     Session = sessionmaker(bind=engine)
     session = Session()

     results = session.query(State).all()

     for result in results:
         print("{}: {}".format(result.id, result.name))

         for city in state.cities:
             print("\t{}: {}".format(city.id, city.name))

    session.close()
