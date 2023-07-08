from datetime import datetime

from engine.capulet_engine import CapuletEngine
from battery import Battery

class Thovex(CapuletEngine):
    def needs_service(self):
        battery = Battery("Nubblin")
        service_threshold_date = self.last_service_date.replace(year=self.last_service_date.year + battery.battery_years())
        if service_threshold_date < datetime.today().date() or self.engine_should_be_serviced():
            return True
        else:
            return False
