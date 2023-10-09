#!/usr/bin/python3
"""upon importation of model package, the module gets executed"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
