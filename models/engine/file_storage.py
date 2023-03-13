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
    CLASSES = []

    def all(self):
        """ return the list of objs """
        return FileStorage.__objects

    def new(self, obj):
        """ creates a new objs to dict """
        if obj.__class__.__name__ not in FileStorage.CLASSES:
            return 'Not a valid object passed'
        try:
            obj_t = obj.to_dict()
            var = f"{obj_t['__class__']}.{obj_t['id']}"
            FileStorage.__objects[var] = obj_t
        except (NameError, AttributeError) as e:
            return "Object is not inheriting from a valid class"

    def save(self):
        """ Serializer: save to storage filesystem """
        with open(FileStorage.__file_path, 'w') as file:
            json.dump(FileStorage.__objects, file)

    def reload(self):
        """ Desrializer: load from storage as dict """
        try:
            with open(FileStorage.__file_path, 'r') as file:
                FileStorage.__objects = json.load(file)
        except FileNotFoundError as error:
            return "File not found"

    def delete(self, key):
        """ deletes an obj based off the key """
        if key.split('.')[0] not in FileStorage.CLASSES:
            return 'key must be a valid class'
        try:
            del FileStorage.__objects[key]
        except AttributeError as e:
            return "Object found for the given key"

    def update(self, key, prop, val):
        """ Updates an obj based given key ref """
        if prop in ['id', 'created_at', 'updated_at']:
            return 'Prop may not updated'
        if type(val) not in [int, str, float]:
            return 'Val type invalid'
        if key.split('.')[0] not in FileStorage.CLASSES:
            return 'key must be a valid model '
        try:
            FileStorage.__objects[key][prop] = val
        except (AttributeError, KeyError):
            return "Invalid Key/Attr"

    def dict_update(self, key, obj):
        """ Updates the dictionary """
        if type(obj) is not dict:
            return 'Not a dictionary'
        for val in obj:
            if val in ['id', 'created_at', 'updated_at']:
                return "Invalid Prop/Attr"
            if type(obj[val]) not in [int, str, float]:
                return "Invalid value type"
            if key.split('.')[0] not in FileStorage.CLASSES:
                return "Invalid Class"
            try:
                FileStorage.__objects[key][val] = obj[val]
            except (AttributeError, KeyError) as e:
                raise Exception('Key/Attr Error')


if __name__ == "__main__":
    pass
