from tires.tires import Tires

class Octoprime():
    def __init__(self, tires):
        self.tires = tires

    def tire_needs_service(self):
        sum = 0
        for pressure in self.tires:
            sum += pressure
        if sum >= 3:
            return True
        return False