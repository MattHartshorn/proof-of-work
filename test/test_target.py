import unittest
from src import target

class TestTarget(unittest.TestCase):
    def test_length(self):
        self.assertEqual(len(target.generate(0)), 32)
    
    def test_all_zeros(self):
        self.assertEqual(target.generate(256), bytes([0]*32))

    def test_all_ones(self):
        self.assertEqual(target.generate(0), bytes([255]*32))
        
    def test_difficulty_8(self):
        self.assertEqual(target.generate(8), bytes([0] + [255]*31))

    def test_difficulty_6(self):
        self.assertEqual(target.generate(6), bytes([3] + [255]*31))

    def test_difficulty_negative(self):
        with self.assertRaises(ValueError):
            target.generate(-1)

    def test_difficulty_257(self):
        with self.assertRaises(ValueError):
            target.generate(257)