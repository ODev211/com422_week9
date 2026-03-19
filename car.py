from vehicle import Vehicle
import math

class Car(Vehicle):

    def calculate_fee(self):
        base_fee = 5.00
        extra_weight = self.weight - 1590

        if extra_weight > 0:
            extra_units = math.ceil(extra_weight / 100)
            base_fee += extra_units * 0.10

        return base_fee