#!/usr/bin/python3
"""
Unit tests for the Amenity class.
"""
import unittest
from models.amenity import Amenity
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    """
    Test cases for Amenity.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.amenity = Amenity()

    def test_inheritance(self):
        """
        Test that Amenity inherits from BaseModel.
        """
        self.assertIsInstance(self.amenity, BaseModel)

    def test_attributes(self):
        """
        Test that Amenity has the required attributes.
        """
        self.assertTrue(hasattr(self.amenity, 'name'))

    def test_attribute_types(self):
        """
        Test that the attributes are of the correct type.
        """
        self.assertIsInstance(self.amenity.name, str)
