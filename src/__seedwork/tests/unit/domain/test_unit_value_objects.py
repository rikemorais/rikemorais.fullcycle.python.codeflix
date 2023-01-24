import unittest
from dataclasses import is_dataclass
from __seedwork.domain.value_objects import UniqueEntityId


class TestUniqueEntityIdUnit(unittest.TestCase):
    
    def test_if_is_a_dataclass(self):
        self.assertTrue(is_dataclass(UniqueEntityId))