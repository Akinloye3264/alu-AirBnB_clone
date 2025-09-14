#!/usr/bin/python3
"""
Unit tests for the BaseModel class.
"""
import unittest
from models.base_model import BaseModel
from models import storage
import datetime


class TestBaseModel(unittest.TestCase):
    """
    Test cases for BaseModel.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.model = BaseModel()
        self.model.save()
        storage.reload()

    def test_instantiation(self):
        """
        Test that BaseModel can be instantiated.
        """
        self.assertIsInstance(self.model, BaseModel)

    def test_id_is_string(self):
        """
        Test that id is a string.
        """
        self.assertIsInstance(self.model.id, str)

    def test_created_at_is_datetime(self):
        """
        Test that created_at is a datetime object.
        """
        self.assertIsInstance(self.model.created_at, datetime.datetime)

    def test_updated_at_is_datetime(self):
        """
        Test that updated_at is a datetime object.
        """
        self.assertIsInstance(self.model.updated_at, datetime.datetime)

    def test_unique_id(self):
        """
        Test that each BaseModel instance has a unique id.
        """
        model1 = BaseModel()
        model2 = BaseModel()
        self.assertNotEqual(model1.id, model2.id)

    def test_str_representation(self):
        """
        Test the string representation of BaseModel.
        """
        expected_str = "[BaseModel] ({}) {}".format(
            self.model.id, self.model.__dict__)
        self.assertEqual(str(self.model), expected_str)

    def test_to_dict_method(self):
        """
        Test the to_dict method.
        """
        model_dict = self.model.to_dict()
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(
            model_dict['created_at'], self.model.created_at.isoformat())
        self.assertEqual(
            model_dict['updated_at'], self.model.updated_at.isoformat())
        self.assertIsInstance(model_dict['created_at'], str)
        self.assertIsInstance(model_dict['updated_at'], str)

    def test_save_method(self):
        """
        Test that save method updates the updated_at attribute.
        """
        old_updated_at = self.model.updated_at
        self.model.save()
        self.assertGreater(self.model.updated_at, old_updated_at)
