#!/usr/bin/python3
"""Module housing the `City` class"""

from models.base_model import BaseModel


class City(BaseModel):
    """Defines a City"""

    state_id = ""
    name = ""
