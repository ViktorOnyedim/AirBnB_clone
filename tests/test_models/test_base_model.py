#!/usr/bin/python3
"""Base Model unittest"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_init(self):
        """test_initialization of BaseModel"""
        model = BaseModel()
        self.assertIsInstance(model, BaseModel)
        self.assertIsInstance(model.id, str)
        self.assertIsInstance(model.created_at, datetime)
        self.assertIsInstance(model.updated_at, datetime)

    def test_str(self):
        model = BaseModel()
        string = f"[BaseModel] ({model.id}) {model.__dict__}"
        self.assertEqual(str(model), string)

    def test_save(self):
        """test save method of BaseModel"""
        model = BaseModel()
        created_at = model.created_at
        model.save()
        self.assertNotEqual(created_at, model.updated_at)

    def test_to_dict(self):
        """test to_dict method of BaseModel"""
        model = BaseModel()
        model_dict = model.to_dict()
        self.assertIsInstance(model_dict, dict)
        self.assertEqual(model_dict['__class__'], 'BaseModel')
        self.assertEqual(model_dict['created_at'], model.created_at.isoformat())
        self.assertEqual(model_dict['updated_at'], model.updated_at.isoformat())
        for key in model_dict:
            self.assertTrue(hasattr(model, key))

if __name__ == '__main__':
    unittest.main()
