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
            try:
                self.id = kwargs['id']
                self.created_at = datetime.fromisoformat(kwargs['created_at'])
                self.updated_at = datetime.fromisoformat(kwargs['updated_at'])
            except KeyError as error:
                print("Dictionary must Contain required attributes as Keys")
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
        return f"[{self.__class__.__name__}] (self.id) {self.to_dict()}"

    def to_dict(self):
        """ DIctionary rep of the obj """
        try:
            t = dict(self.__class__.__dict__)
            check = ['save', 'to_dict']
            s = {r: t[r] for r in t if not r.startswith('_') and r not in check}
            temp = {**self.__dict__, **s}
            temp['created_at'] = self.created_at.isoformat()
            temp['updated_at'] = self.updated_at.isoformat()
            temp['id'] = str(self.id)
            return {**temp, "__class__": self.__class__.__name__}
        except BaseException as e:
            return {'error': str(e)}


if __name__ == "__main__":
    pass
