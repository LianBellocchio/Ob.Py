import unittest
from orbwalker.utils import get_distance, get_closest_object

class TestUtils(unittest.TestCase):
    def test_get_distance(self):
        point1 = (0, 0)
        point2 = (3, 4)
        self.assertEqual(get_distance(point1, point2), 5)
        
        point1 = (-5, 2)
        point2 = (3, -6)
        self.assertAlmostEqual(get_distance(point1, point2), 11.7046999, places=6)
        
        point1 = (1.5, 2.5)
        point2 = (1.5, 2.5)
        self.assertEqual(get_distance(point1, point2), 0)
        
    def test_get_closest_object(self):
        point = (0, 0)
        objects = [(1, 1), (2, 2), (-1, -1), (0, 3)]
        self.assertEqual(get_closest_object(point, objects), (1, 1))
        
        point = (3, 3)
        objects = [(1, 1), (2, 2), (-1, -1), (0, 3)]
        self.assertEqual(get_closest_object(point, objects), (0, 3))
        
        point = (5, 5)
        objects = [(1, 1), (2, 2), (-1, -1), (0, 3)]
        self.assertIsNone(get_closest_object(point, objects))
