#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import time


class TestBaseModel(unittest.TestCase):
    """
    Tests for the BaseModel class functionality.
    """

    def setUp(self):
        """
        Set up a new BaseModel instance for each test.
        """
        self.model = BaseModel()

    def test_id_is_string(self):
        """
        Test that the id attribute is a string.
        """
        self.assertIsInstance(self.model.id, str)

    def test_id_is_unique(self):
        """
        Test that each BaseModel instance has a unique id.
        """
        model_2 = BaseModel()
        self.assertNotEqual(self.model.id, model_2.id)

    def test_created_at_is_datetime(self):
        """
        Test that created_at is a datetime object.
        """
        self.assertIsInstance(self.model.created_at, datetime)

    def test_updated_at_is_datetime(self):
        """
        Test that updated_at is a datetime object.
        """
        self.assertIsInstance(self.model.updated_at, datetime)

    def test_str_representation(self):
        """
        Test the string representation of the BaseModel instance.
        """
        expected_str = f"[{self.model.__class__.__name__}] ({self.model.id}) {self.model.__dict__}"
        self.assertEqual(str(self.model), expected_str)

    def test_save_updates_updated_at(self):
        """
        Test that the save method updates the updated_at attribute.
        """
        old_updated_at = self.model.updated_at
        time.sleep(0.001)  # Ensure a time difference
        self.model.save()
        new_updated_at = self.model.updated_at
        self.assertGreater(new_updated_at, old_updated_at)

    def test_to_dict_returns_dict(self):
        """
        Test that to_dict method returns a dictionary.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict, dict)

    def test_to_dict_contains_correct_keys(self):
        """
        Test that the dictionary contains the required keys.
        """
        model_dict = self.model.to_dict()
        self.assertIn('id', model_dict)
        self.assertIn('created_at', model_dict)
        self.assertIn('updated_at', model_dict)
        self.assertIn('__class__', model_dict)

    def test_to_dict_datetime_are_strings(self):
        """
        Test that created_at and updated_at are in string format.
        """
        model_dict = self.model.to_dict()
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)
