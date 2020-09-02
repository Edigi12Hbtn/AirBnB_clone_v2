#!/usr/bin/python3
""" Defines DBStorage class as another optional engine."""
from sqlalchemy import (create_engine)
from os import environ
from models.base_model import Base
from sqlalchemy.orm import sessionmaker, scoped_session
from models.base_model import BaseModel, Base


class DBStorage:
    """DBStorage engine class."""
    __engine = None
    __session = None

    def __init__(self):
        """init method for DBStorage class."""

        drop = environ['HBNB_ENV']
        host = environ['HBNB_MYSQL_HOST']
        user = environ['HBNB_MYSQL_USER']
        pwd = environ['HBNB_MYSQL_PWD']
        db = environ['HBNB_MYSQL_DB']

        self.__engine = create_engine(
            'mysql+mysqldb://{}:{}@{}:3306/{}'.format(
                user, pwd, host, db), pool_pre_ping=True)
        if drop == 'test':
            Base.metadata.drop_all(bind=self.__engine)

    def all(self, cls=None):
        """method for doing querying."""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        session = self.__session
        classes = [City, State, User, Place, Review, Amenity]
        objs = {}
        query = []

        if cls is not None:
            query.extend(session.query(cls).all())
        else:
            for element in classes:
                query.extend(session.query(element).all())
        for obj in query:
            key = type(obj).__name__ + '.' + obj.id
            objs[key] = obj
        return objs

    def new(self, obj):
        """add the object to the current database session."""
        session = self.__session
        session.add(obj)

    def save(self):
        """commit all changes of the current database session."""
        session = self.__session
        session.commit()

    def delete(self, obj=None):
        """delete from the current database session obj if not None."""
        session = self.__session
        if obj is not None:
            session.delete(obj)

    def reload(self):
        """create tables in database and session."""
        from models.state import State
        from models.city import City
        from models.user import User
        from models.place import Place
        from models.review import Review
        from models.amenity import Amenity
        engine = self.__engine
        Base.metadata.create_all(engine)
        session_factory = sessionmaker(bind=engine, expire_on_commit=False)
        Session = scoped_session(session_factory)
        self.__session = Session()

    def close(self):
        """Call method on the private session attribute (self.__session)."""
        self.__session.close()
