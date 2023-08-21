#!/usr/bin/python3
"""Module housing the `User` class"""

from models.base_model import BaseModel


class User(BaseModel):
    """Defines a user"""

    email = ""
    password = ""
    first_name = ""
    last_name = ""
