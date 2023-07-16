#!/usr/bin/python3
"""Defines the Review class."""
from models.base_model import BaseModel


class Review(BaseModel):
    """
        class Review:
            Attribute:
                place_id : id(str)
                user_id : user id(str)
                text : str

                """

    place_id = ""
    user_id = ""
    text = ""
