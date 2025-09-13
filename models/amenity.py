#!/usr/bin/python3
"""
This module defines the Amenity class.
It inherits from BaseModel.
"""
from models.base_model import BaseModel


class Amenity(BaseModel):
    """
    Amenity class that represents a public amenity.

    Public class attributes:
        name (str): The name of the amenity.
    """
    name = ""
