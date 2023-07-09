from tires.tires import Tires

class Carrigan():
    def __init__(self, tires):
        self.tires = tires

    def tire_needs_service(self):
        for pressure in self.tires:
            if pressure >= 0.9:
                return True
        
        return False