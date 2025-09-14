#!/usr/bin/python3
"""
Unit tests for the User class.
"""
import unittest
from models.user import User
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    """
    Test cases for User.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.user = User()

    def test_inheritance(self):
        """
        Test that User inherits from BaseModel.
        """
        self.assertIsInstance(self.user, BaseModel)

    def test_attributes(self):
        """
        Test that User has the required attributes.
        """
        self.assertTrue(hasattr(self.user, 'email'))
        self.assertTrue(hasattr(self.user, 'password'))
        self.assertTrue(hasattr(self.user, 'first_name'))
        self.assertTrue(hasattr(self.user, 'last_name'))

    def test_attribute_types(self):
        """
        Test that the attributes are of the correct type.
        """
        self.assertIsInstance(self.user.email, str)
        self.assertIsInstance(self.user.password, str)
        self.assertIsInstance(self.user.first_name, str)
        self.assertIsInstance(self.user.last_name, str)
