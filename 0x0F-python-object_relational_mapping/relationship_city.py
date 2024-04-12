#!/usr/bin/python3

"""
python file that contains the class definition of a
City and an instance Base = declarative_base()
"""

from sqlalchemy import Column, ForeignKey, Integer, String

from relationship_state import Base


class City(Base):
    """
    City class that inherits from Base
    """

    __tablename__ = "cities"

    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String(128), nullable=False)
    state_id = Column(Integer, ForeignKey("states.id"), nullable=False)
