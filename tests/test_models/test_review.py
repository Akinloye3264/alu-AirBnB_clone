#!/usr/bin/python3
"""
Unit tests for the Review class.
"""
import unittest
from models.review import Review
from models.base_model import BaseModel


class TestReview(unittest.TestCase):
    """
    Test cases for Review.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.review = Review()

    def test_inheritance(self):
        """
        Test that Review inherits from BaseModel.
        """
        self.assertIsInstance(self.review, BaseModel)

    def test_attributes(self):
        """
        Test that Review has the required attributes.
        """
        self.assertTrue(hasattr(self.review, 'place_id'))
        self.assertTrue(hasattr(self.review, 'user_id'))
        self.assertTrue(hasattr(self.review, 'text'))

    def test_attribute_types(self):
        """
        Test that the attributes are of the correct type.
        """
        self.assertIsInstance(self.review.place_id, str)
        self.assertIsInstance(self.review.user_id, str)
        self.assertIsInstance(self.review.text, str)
