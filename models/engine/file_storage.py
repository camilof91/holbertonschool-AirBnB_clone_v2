#!/usr/bin/python3
"""This module defines a class to manage file storage for hbnb clone"""
import json
from models.review import Review



class FileStorage:
    """This class manages storage of hbnb models in JSON format"""
    __file_path = 'file.json'
    __objects = {}

    # def all(self, cls=None):
    #     """Returns a dictionary of models currently in storage"""
    #     return FileStorage.__objects

    def all(self, cls=None):
        """Returns a dictionary of models currently in storage"""
        if cls:
            same_type = dict()

            for key, obj in self.__objects.items():
                if obj.__class__ == cls:
                    same_type[key] = obj

            return same_type

        return self.__objects

    # def new(self, obj):
    #     """Adds new object to storage dictionary"""
    #     self.all().update({obj.to_dict()['__class__'] + '.' + obj.id: obj})

    def new(self, obj):
        """Adds new object to storage dictionary"""
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"
            self.__objects[key] = obj

    def save(self):
        """Saves storage dictionary to file"""
        with open(FileStorage.__file_path, 'w') as f:
            temp = {}
            temp.update(FileStorage.__objects)
            for key, val in temp.items():
                temp[key] = val.to_dict()
            json.dump(temp, f)

    def reload(self):
        """Loads storage dictionary from file"""
        from models.base_model import BaseModel
        from models.user import User
        from models.place import Place
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.review import Review

        classes = {
                    'BaseModel': BaseModel, 'User': User, 'Place': Place,
                    'State': State, 'City': City, 'Amenity': Amenity,
                    'Review': Review
                  }
        try:
            temp = {}
            with open(FileStorage.__file_path, 'r') as f:
                temp = json.load(f)
                for key, val in temp.items():
                    if key.endswith('.reviews'):
                        place_id = key.split('.')[0].split('.')[-1]
                        place = FileStorage.__objects[f'Place.{place_id}']
                        place.reviews = [classes[val['__class__']]
                                         (**review) for review
                                         in val['reviews']]

                FileStorage.__objects[key] = classes[val['__class__']](**val)
        except FileNotFoundError:
            pass

    def delete(self, obj=None):
        """Delete obj from __objects if it's inside
        """
        if obj:
            key = f"{type(obj).__name__}.{obj.id}"

            if self.__objects[key]:
                del self.__objects[key]
                self.save()

    def get_reviews(self, place_id):
        """Returns a list of Review instances with place_id
        equal to the provided place_id"""
        reviews = []
        for obj in self.__objects.values():
            if isinstance(obj, Review) and obj.place_id == place_id:
                reviews.append(obj)
        return reviews
    
    def close(self):
        """ methot Close added 7 ponint 
        AirBnB clone - Web framework
        """
        self.reload()


