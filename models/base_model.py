"""base_model.py
serves up a base class for db models to inherit
"""
import uuid
from datetime import datetime
from models import storage


class BaseModel:
    """BaseModel
    Base class holding reusable functionailty
    - Serilization
    - Desrialization
    - Intepreter methods
    """

    def __init__(self, *args, **kwargs):
        """Constructor
        for the base class"""
        if kwargs:
            for key in kwargs:
                if key in ['updated_at', 'created_at']:
                    self.__dict__[key] = datetime.strptime(
                        kwargs[key], "%Y-%m-%dT%H:%M:%S.%f")
                else:
                    self.__dict__[key] = kwargs[key]
        else:
            self.id = str(uuid.uuid4())
            self.created_at = datetime.now()
            self.updated_at = datetime.now()
            storage.new(self)

    def save(self):
        """Serializer
        for the base class and its subclasses
        """
        self.updated_at = datetime.now()
        storage.save()

    def __str__(self):
        """ String rep of the obj """
        return f"[{type(self).__name__}] ({self.id}) {self.__dict__}"

    def to_dict(self):
        """ DIctionary rep of the obj """
        temp = self.__dict__.copy()
        temp['created_at'] = temp['created_at'].isoformat()
        temp['updated_at'] = temp['updated_at'].isoformat()
        temp['__class__'] = type(self).__name__
        return temp
