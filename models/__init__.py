#!/usr/bin/python3
"""This module instantiates an object of class Storage"""

import os
from models.engine.file_storage import FileStorage
from models.engine.db_storage import DBStorage

# Use environment variable HBNB_TYPE_STORAGE to determine storage type
storage_type = os.getenv('HBNB_TYPE_STORAGE')

if storage_type == 'db':
    from models.engine.db_storage import DBStorage
    storage = DBStorage()
else:
    from models.engine.file_storage import FileStorage
    storage = FileStorage()

storage.reload()
