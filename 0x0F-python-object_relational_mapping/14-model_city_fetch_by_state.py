#!/usr/bin/python3
""" print all state's name that contains 'a'
"""
import sys
from sqlalchemy import (create_engine)
from sqlalchemy.orm import sessionmaker
from model_state import Base, State
from model_city import City

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2],
                                   sys.argv[3]), pool_pre_ping=True)
    Base.metadata.create_all(engine)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(City.name, City.id,
                          State.name).join(State, City.state_id == State.id)
    for row in query.all():
        print("{}: ({}) {}".format(row[2], row[1], row[0]))
    session.close()
