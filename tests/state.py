#!/usr/bin/python3
"""state.py test module"""

import unittest
from models.state import State


class TestState(unittest.TestCase):
    """state class testing"""

    def test_instantiation(self):
        """function testing instances of user object"""
        obj = State()
        self.assertIsInstance(obj, State)

    def test_attr(self):
        """function testing attributes of the user object"""
        self.obj = State()
        self.assertTrue(hasattr(self.obj, "id"))
        self.assertTrue(hasattr(self.obj, "created_at"))
        self.assertTrue(hasattr(self.obj, "updated_at"))
        self.assertFalse(hasattr(self.obj, "extra"))
        self.assertTrue(self.obj.__class__.__name__, "User")

    def test_save(self):
        """function testing save method"""
        obj = State()
        obj.save()
        self.assertTrue(hasattr(obj, "updated_at"))

    def test_str(self):
        """function testing __str__ method"""
        obj = State()
        obj_str = "[{} ({}) {}".format(
                obj.__class__.__name__,
                obj.id,
                obj.__dict__)


if __name__ == "__main__":
    unittest.main()
