import unittest
from datetime import datetime

from batteries.nubbin import Nubbin
from batteries.spindler import Spindler



class TestNubbin(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 5)

        nubbin = Nubbin(last_service_date)
        self.assertTrue(nubbin.needs_service())

    def test_battery_does_not_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 2)

        nubbin = Nubbin(last_service_date)
        self.assertFalse(nubbin.needs_service())

class TestSpindler(unittest.TestCase):
    def test_battery_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 4)

        spindler = Spindler(last_service_date)
        self.assertTrue(spindler.needs_service())

    def test_battery_does_not_needs_service(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 1)

        spindler = Spindler(last_service_date)
        self.assertFalse(spindler.needs_service())