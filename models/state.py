#!/usr/bin/python3
"""
This module defines the State class.
It inherits from BaseModel.
"""
from models.base_model import BaseModel


class State(BaseModel):
    """
    State class that represents a geographical state.

    Public class attributes:
        name (str): The name of the state.
    """
    name = ""
