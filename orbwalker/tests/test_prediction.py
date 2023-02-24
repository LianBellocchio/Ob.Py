import unittest
from orbwalker.prediction.prediction import Prediction
from orbwalker.utils import Point

class TestPrediction(unittest.TestCase):
    
    def setUp(self):
        self.prediction = Prediction()
        self.target = Point(100, 200)
        self.speed = 200
        self.delay = 0.5
        
    def test_linear_prediction(self):
        # Set up test data
        origin = Point(0, 0)
        direction = Point(1, 1).normalize()
        
        # Perform prediction
        predicted_pos = self.prediction.linear_prediction(origin, direction, self.target, self.speed, self.delay)
        
        # Check predicted position
        self.assertAlmostEqual(predicted_pos.x, 247.412, delta=0.001)
        self.assertAlmostEqual(predicted_pos.y, 347.412, delta=0.001)
        
    def test_circular_prediction(self):
        # Set up test data
        origin = Point(0, 0)
        radius = 500
        
        # Perform prediction
        predicted_pos = self.prediction.circular_prediction(origin, radius, self.target, self.speed, self.delay)
        
        # Check predicted position
        self.assertAlmostEqual(predicted_pos.x, -23.153, delta=0.001)
        self.assertAlmostEqual(predicted_pos.y, 186.523, delta=0.001)
        
    def test_best_prediction(self):
        # Set up test data
        origin = Point(0, 0)
        direction = Point(1, 1).normalize()
        radius = 500
        
        # Perform prediction
        predicted_pos = self.prediction.best_prediction(origin, direction, radius, self.target, self.speed, self.delay)
        
        # Check predicted position
        self.assertAlmostEqual(predicted_pos.x, -23.153, delta=0.001)
        self.assertAlmostEqual(predicted_pos.y, 186.523, delta=0.001)
