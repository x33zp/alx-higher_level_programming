#!/usr/bin/python3
"""
Defines a SQLAlchemy model for the 'cities' table.
"""
from model_state import Base
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy import Column, Integer, String


class City(Base):
    """
    City class
    """
    __tablename__ = 'cities'

    id = Column(Integer, primary_key=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey('states.id'))
