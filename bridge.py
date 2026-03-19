class Bridge:
    MAX_VEHICLES = 20
    MAX_WEIGHT = 30000

    def __init__(self):
        self.vehicles = []

    def calc_total_weight(self):
        return sum(vehicle.get_weight() for vehicle in self.vehicles)

    def add_vehicle(self, vehicle):
        if len(self.vehicles) >= self.MAX_VEHICLES:
            print("Bridge full. Vehicle denied.")
            return False

        if self.calc_total_weight() + vehicle.get_weight() > self.MAX_WEIGHT:
            print("Weight limit exceeded. Vehicle denied.")
            return False

        self.vehicles.append(vehicle)
        print(f"Vehicle added: {vehicle.get_registration_number()}")
        return True

    def remove_vehicle(self, reg_number):
        for vehicle in self.vehicles:
            if vehicle.get_registration_number() == reg_number:
                self.vehicles.remove(vehicle)
                print(f"Vehicle removed: {reg_number}")
                return True
