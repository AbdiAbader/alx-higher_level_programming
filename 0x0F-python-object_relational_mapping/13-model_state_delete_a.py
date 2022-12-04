#!/usr/bin/python3
""" script that lists all State objects that contain the
letter a from the database hbtn_0e_6_usa """


import sys
from model_state import Base, State
from sqlalchemy.engine import create_engine
from sqlalchemy.orm import sessionmaker


if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1], sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    Session = sessionmaker(bind=engine)
    session = Session()
    r = session.query(State).filter(State.name.contains('a')).all()
    for i in r:
        session.delete(i)
    session.commit()
    session.close()
