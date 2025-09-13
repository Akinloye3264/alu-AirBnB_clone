#!/usr/bin/python3
"""This module defines the FileStorage class for object serialization"""

import json
import os
from models.base_model import BaseModel
from models.user import User  




class FileStorage:
    """Serializes instances to a JSON file & deserializes back to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """Sets in __objects the obj with key <obj class name>.id"""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        obj_dict = {key: obj.to_dict() for key, obj in FileStorage.__objects.items()}
        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        if os.path.exists(FileStorage.__file_path):
            try:
                from models.base_model import BaseModel
                from models.user import User

                classes = {
                    "BaseModel": BaseModel,
                    "User": User,
                }

                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                    for key, value in obj_dict.items():
                        class_name = value.get("__class__")
                        if class_name in classes:
                            FileStorage.__objects[key] = classes[class_name](**value)
            except Exception:
                pass
