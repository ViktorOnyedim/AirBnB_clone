#!/usr/bin/python3
"""Base Model unittest"""
import unittest
from models.base_model import BaseModel
from datetime import datetime


class TestBaseModel(unittest.TestCase):
    """Tests for BaseModel class"""

    def test_initialization(self):
        """test_initialization of BaseModel"""
        bm = BaseModel()
        self.assertIsInstance(bm, BaseModel)
        self.assertIsInstance(bm.id, str)
        self.assertIsInstance(bm.created_at, datetime)
        self.assertIsInstance(bm.updated_at, datetime)

    def test_save(self):
        """test save method of BaseModel"""
        bm = BaseModel()
        updated_at = bm.updated_at
        bm.save()
        self.assertNotEqual(updated_at, bm.updated_at)

    def test_to_dict(self):
        """test to_dict method of BaseModel"""
        bm = BaseModel()
        bm_dict = bm.to_dict()
        self.assertIsInstance(bm_dict, dict)
        self.assertEqual(bm_dict['__class__'], 'BaseModel')
        self.assertEqual(bm_dict['created_at'], bm.created_at.isoformat())
        self.assertEqual(bm_dict['updated_at'], bm.updated_at.isoformat())


if __name__ == '__main__':
    unittest.main()
