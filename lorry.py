from vehicle import Vehicle

class Lorry(Vehicle):

    def calculate_fee(self):
        if self.weight > 8000:
            return 15.00