#!/usr/bin/python3
"""Review class"""

from models.base_model import BaseModel
from models.place import Place
from models.user import User


class Review(BaseModel):
    """review object representation"""
    place_id = ""
    user_id = ""
    text = ""

    def __init__(self, *args, **kwargs):
        """ function initializing class instance with base class"""
        super().__init__(self, *args, **kwargs)
