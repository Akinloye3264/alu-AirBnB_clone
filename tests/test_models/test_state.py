#!/usr/bin/python3
"""
Unit tests for the State class.
"""
import unittest
from models.state import State
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    """
    Test cases for State.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.state = State()

    def test_inheritance(self):
        """
        Test that State inherits from BaseModel.
        """
        self.assertIsInstance(self.state, BaseModel)

    def test_attributes(self):
        """
        Test that State has the required attributes.
        """
        self.assertTrue(hasattr(self.state, 'name'))

    def test_attribute_types(self):
        """
        Test that the attributes are of the correct type.
        """
        self.assertIsInstance(self.state.name, str)
