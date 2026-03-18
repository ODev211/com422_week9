from abc import ABC, abstractmethod

# Bridge design pattern
class Vehicle(ABC):
    def __init__(self, registration_number, weight):
        self.registration_number = registration_number
        self.weight = weight

    @abstractmethod
    def calculate_fee(self):
        pass

# Implementations
class Motorbike(Vehicle):
    def calculate_fee(self):
        return 3.00

class Car(Vehicle):
    def calculate_fee(self):
        if self.weight <= 1590:
            return 5.00
        elif self.weight > 1590:
            # For loop to add 10p per every 100kg over the 1590kg limit
            for i in range(int(self.weight/100)):
                return 5.00 + 0.10
        return 5.00

class Lorry(Vehicle):
    def calculate_fee(self):
        return 10.00