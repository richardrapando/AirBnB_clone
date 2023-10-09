#!/usr/bin/python3
"""
BaseModel class
The above class defines all common attributes/methods for other classes
"""

from datetime import datetime
from uuid import uuid4
from models import storage


class BaseModel:
    """ The base class for other classes is defined """

    def __init__(self, *args, **kwargs):
        """ base model is initialized """
        dtf = "%Y-%m-%dT%H:%M:%S.%f"
        if not kwargs:
            self.id = str(uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)
        else:
            for key in kwargs:
                if key in ['created_at', 'updated_at']:
                    setattr(self, key, datetime.strptime(kwargs[key], dtf))
                elif key != '__class__':
                    setattr(self, key, kwargs[key])

    def save(self):
        """ modification of the update "updated_at" to recent time object """
        self.updated_at = datetime.now()
        storage.save()

    def to_dict(self):
        """
        base object represented in dictionary form
        """
        dic = {"__class__": self.__class__.__name__}
        for k, v in self.__dict__.items():
            if isinstance(v, (datetime, )):
                dic[k] = v.isoformat()
            else:
                dic[k] = v
        return dic

    def __str__(self):
        """
        base object represented in string form
        """
        return "[{}] ({}) {}".format(
            self.__class__.__name__,
            self.id,
            self.__dict__)
