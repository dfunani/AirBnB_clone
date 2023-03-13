"""file_storage
stores files to a .json for persistence
responsible for all serialzations
"""
import json


class FileStorage:
    """FileStorage
    abstraction of the file storing engine
    focuses on serialization
    """

    __file_path = "./file.json"
    __objects = {}

    def factory(self):
        """ Create a CLASSES obj """
        from models.base_model import BaseModel
        from models.user import User
        from models.state import State
        from models.city import City
        from models.amenity import Amenity
        from models.place import Place
        from models.review import Review

        return {
              "BaseModel": BaseModel,
              "User": User,
              "Place": Place,
              "State": State,
              "City": City,
              "Amenity": Amenity,
              "Review": Review
          }

    def all(self):
        """ return the list of objs """
        return FileStorage.__objects

    def new(self, obj):
        """ creates a new objs to dict """
        var = f"{type(obj).__name__}.{obj.id}"
        FileStorage.__objects[var] = obj

    def save(self):
        """ Serializer: save to storage filesystem """
        with open(FileStorage.__file_path, 'w') as file:
            temp = {k: v.to_dict() for k, v in FileStorage.__objects.items()}
            json.dump(temp, file)

    def reload(self):
        """ Desrializer: load from storage as dict """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                temp = json.load(file)
                temp = {k: self.factory()[v['__class__']](**v)
                        for k, v in temp.items()}
                FileStorage.__objects = temp
        except FileNotFoundError as error:
            return "File not found"

    def delete(self, key):
        """ deletes an obj based off the key """
        if key.split('.')[0] not in this.factory():
            return 'key must be a valid class'
        del FileStorage.__objects[key]

    def update(self, key, prop, val):
        """ Updates an obj based given key ref """
        if prop in ['id', 'created_at', 'updated_at']:
            return 'Prop may not updated'
        if type(val) not in [int, str, float]:
            return 'Val type invalid'
        if key.split('.')[0] not in this.factory():
            return 'key must be a valid model '
        try:
            setattr(FileStorage.__objects[key], prop, val)
        except (AttributeError, KeyError):
            return "Invalid Key/Attr"

    def dict_update(self, key, obj):
        """ Updates the dictionary """
        if type(obj) is not dict:
            return 'Not a dictionary'
        for val in obj:
            if val in ['id', 'created_at', 'updated_at']:
                continue
            if type(obj[val]) not in [int, str, float]:
                continue
            if key.split('.')[0] not in this.factory():
                continue
            try:
                FileStorage.__objects[key][val] = obj[val]
            except (AttributeError, KeyError) as e:
                continue


if __name__ == "__main__":
    pass
