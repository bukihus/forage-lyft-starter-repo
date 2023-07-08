from datetime import datetime

from engine.sternman_engine import SternmanEngine
from battery import Battery


class Palindrome(SternmanEngine):
    def needs_service(self):
        battery = Battery("Spindler")
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + battery.battery_years())
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
