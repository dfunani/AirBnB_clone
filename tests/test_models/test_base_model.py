"""Test Base Model
using unittesting"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class Test_BaseModel(unittest.TestCase):
    """ Class managing the test cases """
    def setUp(self):
        self.basemodel = BaseModel()

    def test_init(self):
        """ Tests creation of the base model and asserts if it exists """
        self.assertIs(type(self.basemodel), BaseModel)
        self.assertIs(type(self.basemodel.created_at), datetime)
        self.assertIs(type(self.basemodel.updated_at), datetime)
        self.assertIsInstance(self.basemodel.id, str)

    def test_save(self):
        start = self.basemodel.updated_at
        self.basemodel.save()
        end = self.basemodel.updated_at
        self.assertNotEqual(start, end)

    def test_dict(self):
        res = self.basemodel.to_dict()
        self.assertIs(type(res), dict)
        self.assertIn('__class__', res)
        self.assertIn('id', res)
        self.assertIn('created_at', res)
        self.assertIn('updated_at', res)
        self.assertIs(type(res['created_at']), str)
        self.assertIs(type(res['updated_at']), str)

    def test_str_rep(self):
        var2 = r'-[a-z0-9]{4}-[a-z0-9]{12}\) \{.+\}'
        var = r'\[BaseModel\] \([a-z0-9]{8}-[a-z0-9]{4}'
        self.assertRegex(str(self.basemodel), var + var2)

    def test_reinit(self):
        dictionary = self.basemodel.to_dict()
        temp = BaseModel(**dictionary)
        self.assertIsInstance(temp, BaseModel)
        self.assertIs(type(temp.created_at), datetime)
        self.assertIs(type(temp.updated_at), datetime)
        self.assertIs(type(temp.id), str)


if __name__ == "__main__":
    unittest.main()
