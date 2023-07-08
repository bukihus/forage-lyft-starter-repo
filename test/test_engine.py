import unittest
from datetime import datetime

from engine.capulet_engine import CapuletEngine
from engine.sternman_engine import SternmanEngine
from engine.willoughby_engine import WilloughbyEngine


class TestCapuletEngine(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 40000
        last_service_mileage = 9000

        capulet = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(capulet.needs_service())
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 40000
        last_service_mileage = 20000

        capulet = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(capulet.engine_should_be_serviced())


class TestWilloughbyEngine(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 100000
        last_service_mileage = 20000

        willughby = WilloughbyEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertTrue(willughby.engine_should_be_serviced())
    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        current_mileage = 100000
        last_service_mileage = 90000

        capulet = CapuletEngine(last_service_date, current_mileage, last_service_mileage)
        self.assertFalse(capulet.engine_should_be_serviced())


class TestSternmanEngine(unittest.TestCase):
    def test_battery_should_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light = True

        sternman = SternmanEngine(last_service_date, warning_light)
        self.assertTrue(sternman.engine_should_be_serviced())

    def test_battery_should_not_be_serviced(self):
        today = datetime.today().date()
        last_service_date = today.replace(year=today.year - 3)
        warning_light = False

        sternman = SternmanEngine(last_service_date, warning_light)
        self.assertFalse(sternman.engine_should_be_serviced())