#!/usr/bin/python3
"""
Test for storage
"""
from datetime import datetime
import unittest
from time import sleep
import json
from models.engine.file_storage import FileStorage


class TestFileStorage(unittest.TestCase):

    def setUp(self):
        self.storage = FileStorage()

    def tearDown(self):
        if os.path.exists(FileStorage._FileStorage__file_path):
            os.remove(FileStorage._FileStorage__file_path)

    def test_save(self):
        # Test saving objects to file
        # Add some test objects to the storage
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Check if the file exists
        self.assertTrue(os.path.exists(FileStorage._FileStorage__file_path))

    def test_reload(self):
        # Test reloading objects from file
        # Add some test objects to the storage
        obj1 = BaseModel()
        obj2 = User()
        self.storage.new(obj1)
        self.storage.new(obj2)
        self.storage.save()

        # Clear the storage and reload from file
        self.storage._FileStorage__objects = {}
        self.storage.reload()

        # Check if the objects are properly reloaded
        self.assertIn(obj1, self.storage.all().values())
        self.assertIn(obj2, self.storage.all().values())


if __name__ == '__main__':
    unittest.main()
