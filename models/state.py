#!/usr/bin/python3
""" State Module for HBNB project """
from sqlalchemy import Column, Integer, String, ForeignKey
from sqlalchemy.orm import relationship
from models.base_model import BaseModel, Base
from models.city import City
import models
from os import getenv


type_engine = getenv('HBNB_TYPE_STORAGE')


class State(BaseModel, Base):
    """ The city class, contains state ID and name """
    # for dbstorage:
    __tablename__ = 'states'
    if type_engine == 'db':
        name = Column(
            'name',
            String(128),
            nullable=False
        )
        cities = relationship('City', cascade="all, delete", backref="state")
    # for filestorage:
    else:
        name = ''

        @property
        def cities(self):
            """ Getter method for  return all cities of a state"""
            cities = []

            for key, city in models.storage.all(City).items():
                if city.state_id == self.id:
                    cities.append(city)

            return cities
