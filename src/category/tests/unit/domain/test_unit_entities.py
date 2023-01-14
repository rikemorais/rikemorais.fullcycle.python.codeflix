from dataclasses import is_dataclass
from category.domain.entities import Category
from datetime import datetime
import unittest

class TestCategoryUnit(unittest.TestCase):
    
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))
    
    def test_constructor(self):
        category = Category(
            name='Movie', 
            description='some description', 
            is_active=True, 
            created_at=datetime.now()
        )
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertEqual(category.is_active, True)
        self.assertEqual(category.created_at, datetime)