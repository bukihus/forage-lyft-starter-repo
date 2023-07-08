from datetime import datetime

from engine.willoughby_engine import WilloughbyEngine
from battery import Battery

class Rorschach(WilloughbyEngine):
    def needs_service(self):
        battery = Battery("Nubblin")
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + battery.battery_years())
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
