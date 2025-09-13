#!/usr/bin/python3
"""
This module defines the City class.
It inherits from BaseModel.
"""
from models.base_model import BaseModel


class City(BaseModel):
    """
    City class that represents a city.

    Public class attributes:
        state_id (str): The id of the state the city belongs to.
        name (str): The name of the city.
    """
    state_id = ""
    name = ""
