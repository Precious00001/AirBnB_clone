#!/usr/bin/python3
"""Defines the City class."""
from models.base_model import BaseModel


class City(BaseModel):
    """
        city class iherit from base
            Atrribute:
                state_id (str)
                name (str)
    """

    state_id = ""
    name = ""

