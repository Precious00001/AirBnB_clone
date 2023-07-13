#!/usr/bin/python3
"""
file storage modules
"""
import json
from models.base_model import BaseModel
from models.user import User
from models.amenity import Amenity
from models.review import Review
from models.state import State
from models.place import Place
from models.city import City


class FileStorage:
    """Rep of an abstracted storage engine.

    Attr:
        __file_path (str): The name of the file to save objects to.
        __objects (dict): A dictionary of instantiated objects.
    """
    __file_path = "file.json"
    __objects = {}

    def save(self):
        """Serialize __objects to the JSON file __file_path."""
        odict = FileStorage.__objects
        objd = {obj: odict[obj].to_dict() for obj in odict.keys()}
        with open(FileStorage.__file_path, "w") as f:
            json.dump(objd, f)

    def all(self):
        """since __object is private class attribute
        we access it like so."""
        return FileStorage.__objects



    def reload(self):
        """ read from the file, deserialize the dict obtained from the file
        each val from the dict is a dict of args and kwargs of an instance
        each key found represent an instance we check if it
        exit else we create new one
        and append if to the __objects"""
        try:
            with open(FileStorage.__file_path) as f:
                objd = json.load(f)
                for o in objd.values():
                    cls_name = o["__class__"]
                    del o["__class__"]
                    self.new(eval(cls_name)(**o))
        except FileNotFoundError:
            return

    def new(self, obj):
        """
        we add the object to the __objects attribute
        the key is generated as <obj class name>.id
        """
        objcn = obj.__class__.__name__
        FileStorage.__objects["{}.{}".format(objcn, obj.id)] = obj
