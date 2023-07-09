import unittest
from datetime import datetime

from tires.carrigan import Carrigan
from tires.octoprime import Octoprime



class TestCarrigan(unittest.TestCase):
    def test_tire_needs_service(self):
        tires = [0.9, 1, 0, 0.8]

        carrigan = Carrigan(tires)
        self.assertTrue(carrigan.tire_needs_service())

    def test_battery_does_not_needs_service(self):
        tires = [0.8, 0.5, 0, 0.8]

        carrigan = Carrigan(tires)
        self.assertFalse(carrigan.tire_needs_service())


class TestOctoprime(unittest.TestCase):
    def test_tire_needs_service(self):
        tires = [0.9, 1, 0.7, 0.8]

        octoprime = Octoprime(tires)
        self.assertTrue(octoprime.tire_needs_service())

    def test_battery_does_not_needs_service(self):
        tires = [0.8, 0.5, 0, 0.8]

        octoprime = Octoprime(tires)
        self.assertFalse(octoprime.tire_needs_service())