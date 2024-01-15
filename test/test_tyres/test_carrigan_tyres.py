import unittest
from tyres.carrigan import CarriganTyres


class TestCarriganTyres(unittest.TestCase):
    def test_needs_service_true(self):
        sensor_array = [0.5, 1, 0.3, 0.9]
        tyres = CarriganTyres(sensor_array)
        self.assertTrue(tyres.needs_service())

    def test_needs_service_false(self):
        sensor_array = [0.5, 0.8, 0.3, 0.4]
        tyres = CarriganTyres(sensor_array)
        self.assertTrue(tyres.needs_service())