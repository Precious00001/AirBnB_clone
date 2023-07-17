#!/usr/bin/python3
"""Defines unittests for console.py.

Unittest classes:
    TestHBNBCommand_prompting
    TestHBNBCommand_help
    TestHBNBCommand_exit
    TestHBNBCommand_create
    TestHBNBCommand_show
    TestHBNBCommand_all
    TestHBNBCommand_destroy
    TestHBNBCommand_update
"""
import os
import sys
import unittest
from models import storage
from models.engine.file_storage import FileStorage
from console import HBNBCommand
from io import StringIO
from unittest.mock import patch


class TestHBNBCommand(unittest.TestCase):

    @patch('sys.stdout', new_callable=StringIO)
    def test_prompting(self, mock_stdout):
        console = HBNBCommand()
        console.cmdloop()
        self.assertEqual(mock_stdout.getvalue(), "(hbnb) ")

    @patch('sys.stdout', new_callable=StringIO)
    def test_help(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd("help")
        expected_output = "Documented commands (type help <topic>):\n" \
                          "========================================\n" \
                          "EOF  create  destroy  help  quit  show  update\n\n"
        self.assertEqual(mock_stdout.getvalue(), expected_output)

    def test_exit(self):
        console = HBNBCommand()
        self.assertTrue(console.do_quit(""))

    @patch('sys.stdout', new_callable=StringIO)
    def test_create(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd("create BaseModel")
        self.assertIn("BaseModel", mock_stdout.getvalue())

    @patch('sys.stdout', new_callable=StringIO)
    def test_show(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd("show BaseModel 123")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_all(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd("all")
        self.assertEqual(mock_stdout.getvalue(), "[]\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_destroy(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd("destroy BaseModel 123")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_update(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd("update BaseModel 123 email \"test@example.com\"")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_count(self, mock_stdout):
        console = HBNBCommand()
        console.onecmd("count BaseModel")
        self.assertEqual(mock_stdout.getvalue(), "0\n")

    @patch('sys.stdout', new_callable=StringIO)
    def test_default(self, mock_stdout):
        console = HBNBCommand()
        console.default("BaseModel.show(123)")
        self.assertEqual(mock_stdout.getvalue(), "** no instance found **\n")


if __name__ == '__main__':
    unittest.main()
