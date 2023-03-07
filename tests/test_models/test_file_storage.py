"""tests file storage
as a singleton built file storage system
"""
import unittest
from models.base_model import BaseModel
from models import storage

class Test_FileStorage(unittest.TestCase):
    """ test class inehirting from Unittestings TestCase Engine """

    def setUp(self):
        self.bs = BaseModel()

    def test_all(self):
        self.assertIs(type(storage.all()), dict)
        for keys in storage.all():
            self.assertRegex(keys, r'[a-z0-9]+[.][a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}')

    def test_new(self):
        temp_fs = storage.all()
        storage.new(self.bs)
        storage.save()
        storage.reload()
        self.assertTrue(len(storage.all()) - len(temp_fs) == 1)
        temp_fs = storage.all()
        storage.new(BaseModel(**self.bs.to_dict))
        storage.save()
        storage.reload()
        self.assertTrue(len(storage.all()) == len(temp_fs))

if __name__ == "__main__":
    unittest._main()
