from toll_bridge_project.vehicle import Vehicle

class Lorry(Vehicle):
    def calculate_fee(self):
        return 15.00 if self.weight > 8000 else 10.00