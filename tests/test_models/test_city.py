#!/usr/bin/python3
"""
Unit tests for the City class.
"""
import unittest
from models.city import City
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    """
    Test cases for City.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.city = City()

    def test_inheritance(self):
        """
        Test that City inherits from BaseModel.
        """
        self.assertIsInstance(self.city, BaseModel)

    def test_attributes(self):
        """
        Test that City has the required attributes.
        """
        self.assertTrue(hasattr(self.city, 'state_id'))
        self.assertTrue(hasattr(self.city, 'name'))

    def test_attribute_types(self):
        """
        Test that the attributes are of the correct type.
        """
        self.assertIsInstance(self.city.state_id, str)
        self.assertIsInstance(self.city.name, str)
