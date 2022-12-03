#!/usr/bin/python3
"""  python file that contains the class definition of a State and
an instance Base = declarative_base()"""

from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Table, Column, Integer, Numeric, String


Base = declarative_base()


class State(Base):
    """ class State that inherits class Base"""
    __tablename__ = 'states'
    id = Column(Integer, primary_key=True, nullable=False)
    name = Column(String(128), nullable=False)
