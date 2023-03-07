"""Test Base Model
using unittesting"""
import unittest
from models.base_model import BaseModel
from datetime import datetime
import uuid

class Test_BaseModel(unittest.TestCase):
    """ Class managing the test cases """

    def test_init(self):
        """ Tests creation of the base model and asserts if it exists """
        basemodel = BaseModel()
        self.assertIs(type(basemodel), BaseModel)
        self.assertIs(type(basemodel.created_at), datetime)
        self.assertIs(type(basemodel.updated_at), datetime)
        self.assertIsInstance(basemodel.id, uuid.UUID)

    def test_save(self):
        basemodel = BaseModel()
        start = basemodel.updated_at
        basemodel.save()
        end = basemodel.updated_at
        self.assertNotEqual(start, end)

    def test_dict(self):
        basemodel = BaseModel()
        res = basemodel.to_dict()
        self.assertIs(type(res), dict)
        self.assertIn('__class__', res)
        self.assertIn('id', res)
        self.assertIn('created_at', res)
        self.assertIn('updated_at', res)
        self.assertIs(type(res['created_at']), str)
        self.assertIs(type(res['updated_at']), str)

    def test_str_rep(self):
        basemodel = BaseModel()
        self.assertRegex(str(basemodel), r'\[BaseModel\] \([a-z0-9]{8}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{4}-[a-z0-9]{12}\) \{.+\}')

if __name__ == "__main__":
    unittest.main()
