#!/usr/bin/python3
"""File Storage Class"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "objects.json"
    __objects = {}

    def all(self):
        """Returns the dictionary objects"""
        returns self.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: An object to be added to the dictionary
        """
        #for key in obj.keys():
        #if 
        key = f"{type(obj).__name__}.{obj.id}"
        self.__object[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(self.__file_path, mode="w") as f:
            obj_dict = {}
            for key, value in self.__objects.items():
                self.__objects[key] = value.to_dict()
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file __file_path) exists;
        otherwise, do nothing...no exception should be raised
        """
        try:
            with open(self.__file_path, mode="r") as f:
                obj_dict = json.load(f)
                for key, value in obj_dict.items():
                    cls_name, obj_id = key.split(".")
                    cls = globals()[cls_name]
                    obj = cls(**value)
                    self.__objects[key] = obj
        except: FileNotFoundError:
            pass
