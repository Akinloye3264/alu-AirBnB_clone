# models/engine/file_storage.py
import json
from models.user import User  # make sure User is imported
from models.base_model import BaseModel

class FileStorage:
    __file_path = "file.json"
    __objects = {}

    def all(self, cls=None):
        """Returns all objects, or all objects of a class if cls is provided"""
        if cls:
            return {k: v for k, v in self.__objects.items() if isinstance(v, cls)}
        return self.__objects

    def new(self, obj):
        """Adds new object to __objects"""
        key = f"{obj.__class__.__name__}.{obj.id}"
        self.__objects[key] = obj

    def save(self):
        """Serializes __objects to JSON file"""
        obj_dict = {k: v.to_dict() for k, v in self.__objects.items()}
        with open(self.__file_path, "w") as f:
            json.dump(obj_dict, f)

    def reload(self):
        """Deserializes JSON file to __objects"""
        try:
            with open(self.__file_path, "r") as f:
                obj_dict = json.load(f)
            for key, val in obj_dict.items():
                cls_name = val["__class__"]
                cls = globals()[cls_name]  # dynamically get class
                self.__objects[key] = cls(**val)
        except FileNotFoundError:
            pass
