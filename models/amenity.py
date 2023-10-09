#!/usr/bin/python3
"""Amenity class"""

from models.base_model import BaseModel


class Amenity(BaseModel):
    """Amenity object representation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ function initializing class instance with base class"""
        super().__init__(self, *args, **kwargs)
