#!/usr/bin/python3
""" State Module for HBNB project """
from models.base_model import BaseModel, Base
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from os import getenv
import models
from models.city import City

type_db = getenv('HBNB_TYPE_STORAGE')

class State(BaseModel, Base):
    """ State class """
    __tablename__ = 'states'

    if type_db == 'db':  #database
        name = Column(String(128), nullable=False)
        cities = relationship("City", backref='state',
                              cascade="all, delete-orphan")

        @property
        def cities(self):
            """Getter method for class attr cities."""
            return type(self).cities

    else:  # file storage
        name = ''

        @property
        def cities(self):
            """getter method."""
            cities = []

            for key, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return cities
