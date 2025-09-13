#!/usr/bin/python3
"""
This module defines the User class.
It inherits from BaseModel.
"""
from models.base_model import BaseModel


class User(BaseModel):
    """
    User class that represents a user of the application.

    Public class attributes:
        email (str): The email address of the user.
        password (str): The password of the user.
        first_name (str): The first name of the user.
        last_name (str): The last name of the user.
    """
    email = ""
    password = ""
    first_name = ""
    last_name = ""
