#!/usr/bin/python3
"""This module defines the User class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Representation of a User"""
    email = ""
    password = ""
    first_name = ""
    last_name = ""
