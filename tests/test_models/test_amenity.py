#!/usr/bin/python3
"""Unittest module for the Amenity Class."""

import unittest
from datetime import datetime
import time
from models.amenity import Amenity
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestAmenity(unittest.TestCase):
    def setUp(self):
        self.amenity = Amenity()

    def test_attributes_initialization(self):
        self.assertEqual(self.amenity.name, "")

    def test_setting_attributes(self):
        self.amenity.name = "Swimming Pool"
        self.assertEqual(self.amenity.name, "Swimming Pool")

    def test_attributes_type(self):
        self.assertIsInstance(self.amenity.name, str)

    def test_attributes_update(self):
        self.amenity.name = "Gym"
        self.assertEqual(self.amenity.name, "Gym")

    def test_attributes_update_multiple_times(self):
        self.amenity.name = "Spa"
        self.assertEqual(self.amenity.name, "Spa")
        self.amenity.name = "Sauna"
        self.assertEqual(self.amenity.name, "Sauna")

    def test_attributes_empty_string(self):
        self.amenity.name = ""
        self.assertEqual(self.amenity.name, "")


if __name__ == '__main__':
    unittest.main()
