#!/usr/bin/python3
"""State class"""

from models.base_model import BaseModel


class State(BaseModel):
    """state object representation"""
    name = ""

    def __init__(self, *args, **kwargs):
        """ function initializing class instance with base class"""
        super().__init__(self, *args, **kwargs)
