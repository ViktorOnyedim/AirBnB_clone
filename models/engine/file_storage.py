#!/usr/bin/python3
"""File Storage Class"""
import json


class FileStorage:
    """
    Serializes instances to a JSON file and deserializes JSON file to instances
    """
    __file_path = "file.json"
    __objects = {}

    def all(self):
        """Returns the dictionary __objects"""
        return FileStorage.__objects

    def new(self, obj):
        """
        Sets in __objects the obj with key <obj class name>.id

        Args:
            obj: An object to be added to the dictionary
        """
        key = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[key] = obj

    def save(self):
        """Serializes __objects to the JSON file (path: __file_path)"""
        with open(FileStorage.__file_path, mode="w", encoding="utf-8") as f:
            obj_dict = {key: value.to_dict() for key, value in FileStorage.__objects.items()}
            json.dump(obj_dict, f)

    def reload(self):
        """
        Deserializes the JSON file to __objects
        (only if the JSON file __file_path) exists;
        otherwise, do nothing...no exception should be raised
        """
        try:
            with open(FileStorage.__file_path, mode="r", encoding="utf-8") as f:
                obj_dict = json.load(f)
                obj_dict = {key: self.classes()[v["__class__"]](**value) for key, value in obj_dict.items()}
                """cls_name, obj_id = key.split(".")
                cls = globals()[cls_name]
                obj = cls(**value)"""
                FileStorage.__objects[key] = obj
        except FileNotFoundError:
            pass
