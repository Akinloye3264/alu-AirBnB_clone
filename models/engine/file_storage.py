#!/usr/bin/python3
"""FileStorage module - serializes instances to JSON and deserializes back"""

import json
import os


class FileStorage:
    """Serializes instances to a JSON file and deserializes back"""

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
        """Serializes __objects to the JSON file"""
        obj_dict = {}
        for key, obj in FileStorage.__objects.items():
            obj_dict[key] = obj.to_dict()

        with open(FileStorage.__file_path, "w", encoding="utf-8") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes the JSON file to __objects (if it exists)"""
        from models.base_model import BaseModel  # import inside to avoid circular import

        if os.path.exists(FileStorage.__file_path):
            try:
                with open(FileStorage.__file_path, "r", encoding="utf-8") as f:
                    obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name = value["__class__"]
                    if cls_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
            except Exception:
                pass
