#!/usr/bin/python3
"""
Unit tests for the FileStorage class.
"""
import unittest
import os
import json
from models import storage
from models.base_model import BaseModel
from models.user import User


class TestFileStorage(unittest.TestCase):
    """
    Test cases for FileStorage.
    """

    def setUp(self):
        """
        Set up the test case.
        """
        self.file_path = storage._FileStorage__file_path
        with open(self.file_path, 'w') as f:
            f.write("{}")
        storage.reload()

    def tearDown(self):
        """
        Tear down the test case.
        """
        if os.path.exists(self.file_path):
            os.remove(self.file_path)

    def test_all_method(self):
        """
        Test the all() method.
        """
        all_objs = storage.all()
        self.assertIsInstance(all_objs, dict)

    def test_new_method(self):
        """
        Test the new() method.
        """
        user = User()
        storage.new(user)
        key = "User.{}".format(user.id)
        self.assertIn(key, storage.all())

    def test_save_method(self):
        """
        Test the save() method.
        """
        base_model = BaseModel()
        storage.new(base_model)
        storage.save()
        with open(self.file_path, 'r') as f:
            data = json.load(f)
        key = "BaseModel.{}".format(base_model.id)
        self.assertIn(key, data)

    def test_reload_method(self):
        """
        Test the reload() method.
        """
        user = User()
        storage.new(user)
        storage.save()
        storage.reload()
        all_objs = storage.all()
        key = "User.{}".format(user.id)
        self.assertIn(key, all_objs)
        self.assertIsInstance(all_objs[key], User)
