#!/usr/bin/python3
"""Unittest module for the State Class."""

import unittest
from datetime import datetime
import time
from models.state import State
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestState(unittest.TestCase):
    def test_state_attributes(self):
        state = State()
        self.assertEqual(state.name, "")

    def test_state_attribute_assignment(self):
        state = State()
        state.name = "California"
        self.assertEqual(state.name, "California")


if __name__ == "__main__":
    unittest.main()
