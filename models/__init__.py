#!/usr/bin/python3
"""Instantiates a storage object.

-> If the environmental variable 'HBNB_TYPE_STORAGE' is set to 'db',
   instantiates a database storage engine (DBStorage).
-> Otherwise, instantiates a file storage engine (FileStorage).
"""
from os import getenv
from .amenity import Amenity
from .city import City
from .place import Place
from .review import Review
from .state import State
from .user import User

env_db = getenv("HBNB_TYPE_STORAGE")

if env_db == "db":
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()