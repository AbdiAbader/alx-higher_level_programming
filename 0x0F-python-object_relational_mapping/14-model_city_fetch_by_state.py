#!/usr/bin/python3
""" a script 14-model_city_fetch_by_state.py that prints all City
objects from the database hbtn_0e_14_usa:
"""


import sys
from model_state import Base, State
from model_city import City
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker
from sqlalchemy import (create_engine)

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],  sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    query = session.query(State.name, City.id, City.name)
    r = query.filter(City.state_id == State.id).all()
    for i in r:
        print(f"{i[0]}: ({i.id}) {i.name}")
