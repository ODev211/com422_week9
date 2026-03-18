class Car(Vehicle):
    def calculate_fee(self):
        if self.weight <= 1590:
            return 5.00
        elif self.weight > 1590:
            # For loop to add 10p per every 100kg over the 1590kg limit
            for i in range(int(self.weight/100)):
                return 5.00 + 0.10
        return 5.00
