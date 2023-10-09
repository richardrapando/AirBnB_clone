#!/usr/bin/python3
"""City class"""

from models.base_model import BaseModel


class City(BaseModel):
    """city module representation"""

    state_id = ""
    name = ""

    def __init__(self, *args, **kwargs):
        """ function initializing class instance with base class"""
        super().__init__(self, *args, **kwargs)
