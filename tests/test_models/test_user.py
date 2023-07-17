#!/usr/bin/python3
"""Unittest module for the User Class."""

import unittest
from datetime import datetime
import time
from models.user import User
import re
import json
from models.engine.file_storage import FileStorage
import os
from models import storage
from models.base_model import BaseModel


class TestUser(unittest.TestCase):
    def setUp(self):
        """Set up any necessary test dependencies."""
        # Create an instance of User for testing
        self.user = User()

    def test_user_attributes(self):
        """Test the attributes of the User class."""
        self.assertEqual(self.user.email, "")
        self.assertEqual(self.user.password, "")
        self.assertEqual(self.user.first_name, "")
        self.assertEqual(self.user.last_name, "")

    def test_user_inheritance(self):
        """Test if User inherits from BaseModel."""
        self.assertIsInstance(self.user, BaseModel)

if __name__ == '__main__':
    unittest.main()
