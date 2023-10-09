#!/usr/bin/python3
"""FileStorage class that serializes instances to a JSON file
and deserializes JSON file to instances"""

import json
import os
import os.path


class FileStorage:
    """class serializing instances to a JSON file
    and deserializing JSON file to instances"""
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """__objects dictionary returned"""
        return self.__objects

    def new(self, obj):
        """__objects set with key <obj class name>.id"""
        name = "{}.{}".format(obj.__class__.__name__, obj.id)
        self.__objects[name] = obj

    def save(self):
        """__objects serialized to the JSON file (path: __file_path)"""
        my_dict = {}
        for keys, val in self.__objects.items():
            my_dict[keys] = val.to_dict()
        with open(self.__file_path, "w") as json_file:
            json.dump(my_dict, json_file)

    def reload(self):
        """json_file deserialized to objects"""
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        my_dict = {
                "BaseModel": BaseModel,
                "User": User,
                "State": State,
                "City": City,
                "Amenity": Amenity,
                "Place": Place,
                "Review": Review
                }
        if not os.path.isfile(self.__file_path):
            return
        with open(self.__file_path, "r") as file_path:
            objects = json.load(file_path)
            self.__objects = {}
            for key in objects:
                name = key.split(".")[0]
                self.__objects[key] = my_dict[name](**objects[key])
