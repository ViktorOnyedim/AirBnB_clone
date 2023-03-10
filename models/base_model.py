#!/usr/bin/python3

"""Base Model Class"""
from uuid import uuid4
from datetime import datetime
from models import storage


class BaseModel:
    """Defines common attributes and methods for other classes"""
    def __init__(self, *args, **kwargs):
        """Initializes instance attributes

        Args:
            *args: list of arguments
            **kwargs: dict of key/values arguments
        """

        if kwargs:
            for key, value in kwargs.items():
                if key != '__class__':
                    setattr(self, key, value)
            t_fmt = "%Y-%m-%dT%H:%M:%S.%f"
            self.created_at = datetime.strptime(kwargs['created_at'], t_fmt)
            self.updated_at = datetime.strptime(kwargs['updated_at'], t_fmt)
        else:
            self.id = str(uuid4())
            self.created_at = self.updated_at = datetime.now()
            storage.new(self)

    def __str__(self):
        """Returning string representation of BaseModel."""
        return (f"[{type(self).__name__}] ({self.id}) {self.__dict__}")

    def save(self):
        """Updates the instance attr "updated_at" with the current datetime"""
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """Returns dictionary representation of BaseModel"""
        dict_copy = self.__dict__.copy()
        dict_copy['__class__'] = type(self).__name__
        dict_copy['created_at'] = self.created_at.isoformat()
        dict_copy['updated_at'] = self.updated_at.isoformat()
        return dict_copy
