#!/usr/bin/python3
"""Defines the State class."""
import models
from models.base_model import State
from os import getenv
from models.base_model import Base
from models.base_model import BaseModel
from models.city import City
from sqlalchemy import Column
from sqlalchemy import String
from sqlalchemy.orm import relationship



class State(BaseModel, Base):
    """Represents a state for a MySQL database.

    Inherits from SQLAlchemy Base and links to the MySQL table states.

    Attributes:
        __tablename__ (str): The name of the MySQL table to store States.
        name (sqlalchemy String): The name of the State.
        cities (sqlalchemy relationship): The State-City relationship.
    """
    storage = getenv("HBNB_TYPE_STORAGE")

    if storage is None:
        storage = "fs"

    __tablename__ = "states"
    name = Column(String(128), nullable=False)
    cities = relationship("City", backref="state", cascade="delete")

    if getenv("HBNB_TYPE_STORAGE") != "db":
        @property
        def cities(self):
            """Get a list of all related Cities."""
            city_l = []
            for city in list(models.storage.all(City).values()):
                if city.state_id == self.id:
                    city_l.append(city)
            return city_l

    if storage == 'db':
        cities = relationship('City', backref='state', cascade='all, delete')
