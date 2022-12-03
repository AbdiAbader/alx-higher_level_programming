#!/usr/bin/python3
"""  script that lists all State objects from the
database hbtn_0e_6_usa """


import sys
from model_state import Base, State
from sqlalchemy.sql import select
from sqlalchemy import create_engine, engine
from sqlalchemy import text

if __name__ == "__main__":
    engine = create_engine('mysql+mysqldb://{}:{}@localhost/{}'
                           .format(sys.argv[1],  sys.argv[2], sys.argv[3]),
                           pool_pre_ping=True)
    result = engine.execute(text("select * from states"))
    for row in result:
        print(f'{row.id}: {row.name}')
