class Bridge:
    def __init__(self):
        self.vehicles = []
        self.MAX_VEHICLES = 20
        self.MAX_WEIGHT = 30000

    def calc_total_weight(self):
        return sum(v.weight for v in self.vehicles)

    def add_vehicle(self, vehicle):
        if len(self.vehicles) >= self.MAX_VEHICLES:
            return False
        if (self.calc_total_weight() + vehicle.weight) > self.MAX_WEIGHT:
            return False

        self.vehicles.append(vehicle)
        return True

    def remove_vehicle(self, reg_number):
        self.vehicles = [v for v in self.vehicles if v.registration_number != reg_number]