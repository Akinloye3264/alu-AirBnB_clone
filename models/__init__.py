#!/usr/bin/python3
"""Make models a package and set up storage"""

from models.engine.file_storage import FileStorage

storage = FileStorage()
storage.reload()
