import unittest
from category.domain.entities import Category
from dataclasses import is_dataclass
from datetime import datetime

class TestCategoryUnit(unittest.TestCase):
    
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(Category))
    
    def test_constructor(self):
        category = Category(
            name = 'Movie', 
            description = 'Some Description', 
            is_active = True, 
            created_at = datetime.now()
        )
        self.assertEqual(category.name, 'Movie')
        self.assertEqual(category.description, 'Some Description')
        self.assertEqual(category.is_active, True)
        self.assertIsInstance(category.created_at, datetime)