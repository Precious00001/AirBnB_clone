#!/usr/bin/python3
"""Unittest module for the City Class."""

import unittest
from datetime import datetime
import time
from models.city import City
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestCity(unittest.TestCase):
    def test_attributes(self):
        city = BaseModel()
        self.assertEqual(city.state_id, "")
        self.assertEqual(city.name, "")

    def test_set_attributes(self):
        city = BaseModel()
        city.state_id = "CA"
        city.name = "San Francisco"
        self.assertEqual(city.state_id, "CA")
        self.assertEqual(city.name, "San Francisco")

    def test_str_representation(self):
        city = BaseModel()
        city.state_id = "NY"
        city.name = "New York"
        expected_str =
        "[BaseModel] (id={} {'state_id': 'OYO', 'name': 'Oyo'}".format(city.id)
        self.assertEqual(str(city), expected_str)

    def test_to_dict_method(self):
        city = BaseModel()
        city.state_id = "TX"
        city.name = "Austin"
        city_dict = city.to_dict()
        expected_dict = {
            "id": city.id,
            "state_id": "TX",
            "name": "Austin",
            "__class__": "BaseModel"
        }
        self.assertDictEqual(city_dict, expected_dict)


if __name__ == "__main__":
    unittest.main()
