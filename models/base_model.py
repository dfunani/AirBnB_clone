"""base_model.py
serves up a base class for db models to inherit
"""
import uuid
from datetime import datetime

class BaseModel():
    """BaseModel
    Base class holding reusable functionailty
    - Serilization
    - Desrialization
    - Intepreter methods
    """

    def __init__(self):
        """Constructor
        for the base class"""
        self.id = uuid.uuid4()
        self.created_at = datetime.now()
        self.updated_at = datetime.now()

    def save(self):
        """Serializer
        for the base class and its subclasses
        """
        self.updated_at = datetime.now()

    def __str__(self):
        """ String rep of the obj """
        return f"[{self.__class__.__name__}] ({str(self.id)}) {self.__dict__}"

    def to_dict(self):
        """ DIctionary rep of the obj """
        temp = {**self.__dict__}
        temp['created_at'] = self.created_at.isoformat()
        temp['updated_at'] = self.updated_at.isoformat()
        temp['id'] = str(self.id)
        return {**temp, "__class__": self.__class__.__name__}
