#!/usr/bin/python3
"""
This module defines the FileStorage class for
serializes and deserializes instances to a JSON file.
"""
import json
from models.base_model import BaseModel
from models.user import User


class FileStorage:
    """
    Manages storage of models in JSON format.

    Private class attributes:
        __file_path (str): Path to the JSON file.
        __objects (dict): A dictionary to store all objects by `<class name>.<id>`.
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects."""
        return FileStorage.__objects

    def new(self, obj):
        """Sets a new object in __objects with key <obj class name>.id."""
        key = "{}.{}".format(obj.__class__.__name__, obj.id)
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file."""
        temp_dict = {}
        for key, value in FileStorage.__objects.items():
            temp_dict[key] = value.to_dict()
        with open(FileStorage.__file_path, 'w', encoding='utf-8') as f:
            json.dump(temp_dict, f, indent=4)

    def reload(self):
        """Deserializes the JSON file to __objects."""
        try:
            with open(FileStorage.__file_path, 'r', encoding='utf-8') as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    class_name = value["__class__"]
                    if class_name == "BaseModel":
                        FileStorage.__objects[key] = BaseModel(**value)
                    elif class_name == "User":
                        FileStorage.__objects[key] = User(**value)
        except FileNotFoundError:
            pass
